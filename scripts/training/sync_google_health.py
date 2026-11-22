#!/usr/bin/env python3
"""Sync swimming and gym workouts from Google Health API v4 (Pixel Watch 2) to Obsidian logs.

Zero-dependency Python 3.12+ CLI using Google OAuth 2.0 Authorization Code Flow with PKCE.
Credentials and tokens are stored outside this public repository in:
    ~/.config/google-health-sync/config.json
    ~/.config/google-health-sync/tokens.json
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import http.server
import json
import os
import re
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_HEALTH_EXERCISE_URL = (
    "https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints"
)

DEFAULT_CONFIG_DIR = Path.home() / ".config" / "google-health-sync"
DEFAULT_REDIRECT_URI = "http://127.0.0.1:8765/callback"
DEFAULT_SCOPE = (
    "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly"
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LOGS_DIR = REPO_ROOT / "Training" / "Logs"

SWIM_KEYWORDS = ("swim",)
GYM_KEYWORDS = (
    "weight",
    "strength",
    "workout",
    "gym",
    "circuit",
    "core",
    "functional",
    "bootcamp",
    "crossfit",
    "calisthenics",
    "lifting",
)


@dataclass(frozen=True)
class GoogleHealthConfig:
    """Google Cloud OAuth 2.0 client configuration loaded from outside the repo."""

    client_id: str
    client_secret: str
    redirect_uri: str = DEFAULT_REDIRECT_URI


@dataclass(frozen=True)
class WorkoutActivity:
    """Normalized workout record extracted from Google Health API v4 exercise dataPoints."""

    data_point_id: str
    discipline: str  # "swim" | "gym" | "other"
    activity_name: str
    exercise_type: str
    start_time: datetime
    duration_min: float
    distance_m: float | None
    avg_hr: int | None
    calories: int | None
    active_zone_minutes: int | None


def _write_secure_json(path: Path, payload: dict[str, Any]) -> None:
    """Write JSON to disk with owner-only permissions (0600)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    os.chmod(path.parent, 0o700)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    os.chmod(path, 0o600)


def load_config(config_dir: Path) -> GoogleHealthConfig:
    """Load OAuth client config from ~/.config/google-health-sync/config.json.

    Supports either a flat JSON object (`client_id`, `client_secret`) or a raw
    Google Cloud Console downloaded OAuth JSON (`installed` or `web` key).
    """
    config_path = config_dir / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found at {config_path}. "
            "Run `python3 scripts/training/sync_google_health.py init` first."
        )

    raw = json.loads(config_path.read_text(encoding="utf-8"))
    data = raw.get("installed") or raw.get("web") or raw
    client_id = str(data.get("client_id", "")).strip()
    client_secret = str(data.get("client_secret", "")).strip()
    redirect_uri = str(data.get("redirect_uri", DEFAULT_REDIRECT_URI)).strip()

    if not client_id or not client_secret or "YOUR_" in client_id:
        raise ValueError(
            f"Please fill in `client_id` and `client_secret` in {config_path}."
        )
    return GoogleHealthConfig(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
    )


def _post_token(form_data: dict[str, str]) -> dict[str, Any]:
    encoded = urllib.parse.urlencode(form_data).encode("utf-8")
    request = urllib.request.Request(
        GOOGLE_TOKEN_URL,
        data=encoded,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload: dict[str, Any] = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Google OAuth token request failed ({exc.code}): {body}"
        ) from exc

    expires_in = int(payload.get("expires_in", 3600))
    payload["expires_at"] = int(time.time()) + expires_in - 60
    return payload


def _generate_pkce_pair() -> tuple[str, str]:
    verifier = secrets.token_urlsafe(64)
    digest = hashlib.sha256(verifier.encode("ascii")).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return verifier, challenge


def cmd_init(config_dir: Path) -> int:
    """Create a starter config.json outside the repository."""
    config_path = config_dir / "config.json"
    if config_path.exists():
        print(f"Config already exists at {config_path}")
        return 0

    starter = {
        "client_id": "YOUR_GOOGLE_CLOUD_CLIENT_ID.apps.googleusercontent.com",
        "client_secret": "YOUR_GOOGLE_CLOUD_CLIENT_SECRET",
        "redirect_uri": DEFAULT_REDIRECT_URI,
    }
    _write_secure_json(config_path, starter)
    print(f"Created {config_path} (permissions 0600).")
    print(
        "Paste your Google Cloud OAuth credentials (or copy your downloaded "
        "client_secret JSON to this path), then run `auth`."
    )
    return 0


def cmd_auth(config_dir: Path) -> int:
    """Run local Google OAuth 2.0 Authorization Code + PKCE flow and save tokens."""
    config = load_config(config_dir)
    parsed_redirect = urllib.parse.urlparse(config.redirect_uri)
    host = parsed_redirect.hostname or "127.0.0.1"
    port = parsed_redirect.port or 8765
    expected_path = parsed_redirect.path or "/callback"

    verifier, challenge = _generate_pkce_pair()
    state = secrets.token_urlsafe(24)

    auth_params = {
        "response_type": "code",
        "client_id": config.client_id,
        "redirect_uri": config.redirect_uri,
        "scope": DEFAULT_SCOPE,
        "access_type": "offline",
        "prompt": "consent",
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "state": state,
    }
    auth_url = f"{GOOGLE_AUTH_URL}?{urllib.parse.urlencode(auth_params)}"

    received: dict[str, str] = {}

    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            req_url = urllib.parse.urlparse(self.path)
            if req_url.path != expected_path:
                self.send_response(404)
                self.end_headers()
                return

            qs = urllib.parse.parse_qs(req_url.query)
            if "error" in qs:
                received["error"] = qs["error"][0]
            elif "code" in qs:
                received["code"] = qs["code"][0]
                received["state"] = qs.get("state", [""])[0]

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h2>Google Health authorization received.</h2>"
                b"<p>You can close this tab and return to your terminal.</p>"
                b"</body></html>"
            )

        def log_message(self, format: str, *args: object) -> None:
            return

    server = http.server.HTTPServer((host, port), CallbackHandler)
    print("Opening browser for Google Health API authorization...")
    print(f"If it does not open automatically, visit:\n{auth_url}\n")
    webbrowser.open(auth_url)

    try:
        while not received:
            server.handle_request()
    finally:
        server.server_close()

    if "error" in received:
        raise RuntimeError(f"Google authorization failed: {received['error']}")
    if received.get("state") != state:
        raise RuntimeError("OAuth state mismatch; aborting authorization.")

    tokens = _post_token(
        {
            "client_id": config.client_id,
            "client_secret": config.client_secret,
            "grant_type": "authorization_code",
            "redirect_uri": config.redirect_uri,
            "code": received["code"],
            "code_verifier": verifier,
        }
    )
    tokens_path = config_dir / "tokens.json"
    _write_secure_json(tokens_path, tokens)
    print(f"Authentication successful! Tokens saved to {tokens_path} (0600).")
    return 0


def get_valid_access_token(config_dir: Path, config: GoogleHealthConfig) -> str:
    """Return a valid Google OAuth access token, refreshing it if expired."""
    tokens_path = config_dir / "tokens.json"
    if not tokens_path.exists():
        raise FileNotFoundError(
            f"Tokens not found at {tokens_path}. "
            "Run `python3 scripts/training/sync_google_health.py auth` first."
        )

    tokens: dict[str, Any] = json.loads(tokens_path.read_text(encoding="utf-8"))
    if int(tokens.get("expires_at", 0)) > int(time.time()):
        return str(tokens["access_token"])

    refresh_token = str(tokens.get("refresh_token", "")).strip()
    if not refresh_token:
        raise RuntimeError(
            "Missing refresh_token; re-run `python3 scripts/training/sync_google_health.py auth`."
        )

    refreshed = _post_token(
        {
            "client_id": config.client_id,
            "client_secret": config.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
    )
    if "refresh_token" not in refreshed:
        refreshed["refresh_token"] = refresh_token
    _write_secure_json(tokens_path, refreshed)
    return str(refreshed["access_token"])


def fetch_exercise_data_points(
    access_token: str,
    after_date: str,
    page_size: int = 100,
) -> list[dict[str, Any]]:
    """Fetch exercise dataPoints from Google Health API v4 with pagination."""
    all_points: list[dict[str, Any]] = []
    page_token: str | None = None
    filter_expr = f'interval.start_time >= "{after_date}T00:00:00Z"'

    while True:
        params: dict[str, str] = {
            "pageSize": str(page_size),
            "filter": filter_expr,
        }
        if page_token:
            params["pageToken"] = page_token

        url = f"{GOOGLE_HEALTH_EXERCISE_URL}?{urllib.parse.urlencode(params)}"
        request = urllib.request.Request(
            url,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload: dict[str, Any] = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(
                f"Google Health API request failed ({exc.code}): {body}"
            ) from exc

        all_points.extend(payload.get("dataPoints", []))
        next_token = payload.get("nextPageToken")
        if not next_token:
            break
        page_token = str(next_token)

    return all_points


def _parse_protobuf_seconds(duration_str: Any) -> float | None:
    """Parse protobuf Duration strings such as '1800s' or '-3600.5s' into seconds."""
    if duration_str is None:
        return None
    text = str(duration_str).strip()
    if not text:
        return None
    if text.endswith("s"):
        text = text[:-1]
    try:
        return float(text)
    except ValueError:
        return None


def _parse_local_datetime(timestamp_str: str, utc_offset_str: Any) -> datetime:
    """Parse RFC 3339 timestamp and apply optional protobuf startUtcOffset."""
    dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
    offset_sec = _parse_protobuf_seconds(utc_offset_str)
    if offset_sec is not None:
        tz = timezone(timedelta(seconds=offset_sec))
        return dt.astimezone(tz)
    return dt


def classify_discipline(exercise_type: str, display_name: str) -> str:
    """Map Google Health exerciseType / displayName to 'swim', 'gym', or 'other'."""
    combined = f"{exercise_type} {display_name}".lower()
    if any(keyword in combined for keyword in SWIM_KEYWORDS):
        return "swim"
    if any(keyword in combined for keyword in GYM_KEYWORDS):
        return "gym"
    return "other"


def _to_optional_int(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return int(round(float(value)))
    except (TypeError, ValueError):
        return None


def parse_data_point(raw: dict[str, Any]) -> WorkoutActivity | None:
    """Convert a raw Google Health v4 exercise dataPoint into a WorkoutActivity."""
    resource_name = str(raw.get("name", "")).strip()
    data_point_id = resource_name.rsplit("/", 1)[-1] if resource_name else ""
    exercise = raw.get("exercise")
    if not data_point_id or not isinstance(exercise, dict):
        return None

    interval = exercise.get("interval", {})
    start_raw = str(interval.get("startTime", "")).strip()
    if not start_raw:
        return None

    start_time = _parse_local_datetime(start_raw, interval.get("startUtcOffset"))
    duration_sec = _parse_protobuf_seconds(exercise.get("activeDuration"))
    if duration_sec is None and interval.get("endTime"):
        end_time = _parse_local_datetime(
            str(interval["endTime"]), interval.get("endUtcOffset")
        )
        duration_sec = max(0.0, (end_time - start_time).total_seconds())
    duration_min = round((duration_sec or 0.0) / 60.0, 1)

    exercise_type = str(exercise.get("exerciseType", "")).strip()
    display_name = (
        str(exercise.get("displayName", "")).strip()
        or exercise_type.replace("_", " ").title()
        or "Workout"
    )

    metrics = exercise.get("metricsSummary") or {}
    dist_mm = metrics.get("distanceMillimeters")
    distance_m: float | None = None
    if dist_mm is not None:
        try:
            dist_val = float(dist_mm) / 1000.0
            distance_m = dist_val if dist_val > 0 else None
        except (TypeError, ValueError):
            distance_m = None

    return WorkoutActivity(
        data_point_id=data_point_id,
        discipline=classify_discipline(exercise_type, display_name),
        activity_name=display_name,
        exercise_type=exercise_type,
        start_time=start_time,
        duration_min=duration_min,
        distance_m=distance_m,
        avg_hr=_to_optional_int(metrics.get("averageHeartRateBeatsPerMinute")),
        calories=_to_optional_int(metrics.get("caloriesKcal")),
        active_zone_minutes=_to_optional_int(metrics.get("activeZoneMinutes")),
    )


def _format_swim_pace(distance_m: float | None, duration_min: float) -> str:
    if not distance_m or distance_m <= 0 or duration_min <= 0:
        return "__:__ / 100m"
    seconds_per_100m = (duration_min * 60.0) / (distance_m / 100.0)
    mins = int(seconds_per_100m // 60)
    secs = int(round(seconds_per_100m % 60))
    if secs == 60:
        mins += 1
        secs = 0
    return f"{mins}:{secs:02d} / 100m"


def render_workout_markdown(workout: WorkoutActivity) -> str:
    """Render a vault-compliant Obsidian markdown log (no YAML frontmatter)."""
    created_str = workout.start_time.strftime("%Y-%m-%d %H:%M")
    date_str = workout.start_time.strftime("%Y-%m-%d")
    hr_str = f"Avg {workout.avg_hr} bpm" if workout.avg_hr is not None else "Avg __ bpm"
    cal_str = f"{workout.calories} kcal" if workout.calories is not None else "__ kcal"
    azm_line = (
        f"- **Active Zone Minutes:** {workout.active_zone_minutes}\n"
        if workout.active_zone_minutes is not None
        else ""
    )

    if workout.discipline == "swim":
        dist_str = (
            f"{int(round(workout.distance_m))} m"
            if workout.distance_m is not None
            else "__ m"
        )
        pace_str = _format_swim_pace(workout.distance_m, workout.duration_min)
        return (
            f"Created: {created_str}\n"
            "#training/swim_log #note\n\n"
            f"**{date_str} — {workout.activity_name}** — Imported from Pixel Watch 2 / Google Health.\n\n"
            "## Session Overview\n\n"
            f"- **Date:** {date_str}\n"
            "- **Session Type:** (Zurileu Team / Weekend Long / Solo)\n"
            "- **Pool Length:** (25m / 50m)\n"
            f"- **Total Distance:** {dist_str}\n"
            f"- **Duration:** {workout.duration_min:g} min\n"
            f"- **Average Pace:** {pace_str}\n"
            f"- **Heart Rate (Pixel Watch 2 / Google Health):** {hr_str}\n"
            f"- **Calories:** {cal_str}\n"
            f"{azm_line}"
            "- **RPE (1–10):**\n"
            "- **Data Source:** Google Health API v4\n"
            f"- **Google Health ID:** `{workout.data_point_id}`\n\n"
            "---\n\n"
            "## Workout Breakdown\n\n"
            "- **Warm-Up:**\n"
            "- **Pre-Set / Drills:**\n"
            "- **Main Set:**\n"
            "- **Cool-Down:**\n\n"
            "---\n\n"
            "## Technique, Body & Recovery Notes\n\n"
            "- **Technique Cues / Focus:**\n"
            "- **Shoulders & Joint Feel:** (Fresh / Tight / Sore)\n"
            "- **Energy & Pacing Notes:**\n"
            "- **Next Session Adjustments:**\n\n"
            "---\n\n"
            "## See Also\n\n"
            "- [[Training Dashboard]]\n"
            "- [[Training/Logs/Training Data and Logs Overview|Training Data and Logs Overview]]\n"
            "- [[Training/Swimming/Workouts/Weekend Swim Workouts|Weekend Swim Workouts]]\n\n"
            "#### Tags\n"
            "#training #swimming #swim_log\n"
        )

    return (
        f"Created: {created_str}\n"
        "#training/gym_log #note\n\n"
        f"**{date_str} — {workout.activity_name}** — Imported from Pixel Watch 2 / Google Health.\n\n"
        "## Session Overview\n\n"
        f"- **Date:** {date_str}\n"
        "- **Program / Split:** (Full Body A / Full Body B / Custom)\n"
        f"- **Duration:** {workout.duration_min:g} min\n"
        f"- **Heart Rate (Pixel Watch 2 / Google Health):** {hr_str}\n"
        f"- **Calories:** {cal_str}\n"
        f"{azm_line}"
        "- **RPE (1–10):**\n"
        "- **Pre-Session Mobility Completed:** (Yes / Partial / No)\n"
        "- **Data Source:** Google Health API v4\n"
        f"- **Google Health ID:** `{workout.data_point_id}`\n\n"
        "---\n\n"
        "## Exercise Log\n\n"
        "| Exercise | Sets x Reps | Load (kg) | RIR | Notes |\n"
        "| :--- | :--- | :--- | :---: | :--- |\n"
        "| | | | | |\n\n"
        "---\n\n"
        "## Joint Health & Progression Notes\n\n"
        "- **Shoulders / Back / Knees Check:** (Pain-free / Tight / Sore)\n"
        "- **Fatigue Impact on Upcoming Swim:** (Low / Moderate / High)\n"
        "- **Next Session Progression:**\n\n"
        "---\n\n"
        "## See Also\n\n"
        "- [[Training Dashboard]]\n"
        "- [[Training/Logs/Training Data and Logs Overview|Training Data and Logs Overview]]\n"
        "- [[Training/Gym/Programs/Two-Day Gym Program|Two-Day Gym Program]]\n\n"
        "#### Tags\n"
        "#training #gym #gym_log #strength_training\n"
    )


def find_existing_ids(logs_dir: Path) -> set[str]:
    """Scan Training/Logs/*.md for previously imported Google Health IDs."""
    ids: set[str] = set()
    if not logs_dir.exists():
        return ids
    pattern = re.compile(r"Google Health ID:\*\*\s*`?([^\s`]+)`?")
    for md_file in logs_dir.glob("*.md"):
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        for match in pattern.finditer(text):
            ids.add(match.group(1))
    return ids


def target_log_path(logs_dir: Path, workout: WorkoutActivity) -> Path:
    """Compute a collision-free filename in Training/Logs/."""
    date_str = workout.start_time.strftime("%Y-%m-%d")
    label = "Swim" if workout.discipline == "swim" else "Gym"
    candidate = logs_dir / f"{date_str} - {label}.md"
    if not candidate.exists():
        return candidate
    time_suffix = workout.start_time.strftime("%H%M")
    return logs_dir / f"{date_str} - {label} {time_suffix}.md"


def cmd_sync(
    config_dir: Path,
    logs_dir: Path,
    after_date: str,
    dry_run: bool,
    include_all: bool,
) -> int:
    """Fetch Google Health workouts and write new Obsidian markdown logs."""
    config = load_config(config_dir)
    access_token = get_valid_access_token(config_dir, config)
    raw_points = fetch_exercise_data_points(access_token, after_date=after_date)

    existing_ids = find_existing_ids(logs_dir)
    created_count = 0
    skipped_existing = 0
    skipped_other = 0

    for raw in raw_points:
        workout = parse_data_point(raw)
        if workout is None:
            continue
        if not include_all and workout.discipline not in ("swim", "gym"):
            skipped_other += 1
            continue
        if workout.data_point_id in existing_ids:
            skipped_existing += 1
            continue

        dest = target_log_path(logs_dir, workout)
        content = render_workout_markdown(workout)
        if dry_run:
            print(
                f"[DRY RUN] Would create {dest.relative_to(REPO_ROOT)} "
                f"({workout.activity_name}, {workout.duration_min:g} min, "
                f"id={workout.data_point_id})"
            )
        else:
            logs_dir.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
            print(f"Created {dest.relative_to(REPO_ROOT)}")

        existing_ids.add(workout.data_point_id)
        created_count += 1

    print(
        f"Sync complete (after {after_date}): "
        f"{created_count} {'planned' if dry_run else 'created'}, "
        f"{skipped_existing} already imported, "
        f"{skipped_other} non-swim/gym skipped."
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Sync Pixel Watch 2 / Google Health API v4 workouts into Training/Logs/."
    )
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=DEFAULT_CONFIG_DIR,
        help=f"Directory storing config.json and tokens.json (default: {DEFAULT_CONFIG_DIR})",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init", help="Create starter config.json outside the repo")
    subparsers.add_parser("auth", help="Authenticate with Google OAuth 2.0 (PKCE)")

    sync_parser = subparsers.add_parser("sync", help="Fetch and import new workouts")
    sync_parser.add_argument(
        "--days",
        type=int,
        default=30,
        help="Lookback window in days if --after is not set (default: 30)",
    )
    sync_parser.add_argument(
        "--after",
        type=str,
        default=None,
        help="Fetch exercises on/after YYYY-MM-DD (overrides --days)",
    )
    sync_parser.add_argument(
        "--logs-dir",
        type=Path,
        default=DEFAULT_LOGS_DIR,
        help=f"Destination Obsidian logs folder (default: {DEFAULT_LOGS_DIR})",
    )
    sync_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview files that would be created without writing to disk",
    )
    sync_parser.add_argument(
        "--include-all",
        action="store_true",
        help="Import all Google Health exercise types instead of only swim/gym",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "init":
        return cmd_init(args.config_dir)
    if args.command == "auth":
        return cmd_auth(args.config_dir)
    if args.command == "sync":
        after_date = (
            args.after or (date.today() - timedelta(days=args.days)).isoformat()
        )
        return cmd_sync(
            config_dir=args.config_dir,
            logs_dir=args.logs_dir,
            after_date=after_date,
            dry_run=args.dry_run,
            include_all=args.include_all,
        )
    return 1


if __name__ == "__main__":
    sys.exit(main())
