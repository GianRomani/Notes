# Google Health API v4 (Pixel Watch 2) Training Sync

Zero-dependency Python CLI that imports swimming and gym workouts from the **Google Health API (`health.googleapis.com/v4`)** into `Training/Logs/` as Obsidian markdown notes matching `Swim Log Template.md` and `Gym Log Template.md`.

> **Security:** OAuth credentials and tokens are stored strictly outside this public repository in `~/.config/google-health-sync/` (`0600` permissions). This `scripts/` directory is excluded from the Netlify/Zola website build in `netlify.toml`.

## One-Time Setup (Google Cloud Console)

### 1. Create a Google Cloud Project & Enable the Google Health API

1. Open the [Google Cloud Console](https://console.cloud.google.com/) and create (or select) a personal project (e.g. `personal-training-sync`).
2. Go to **APIs & Services → Library**, search for **Google Health API** (`health.googleapis.com`), and enable it.

### 2. Configure the OAuth Consent Screen (Keep in Testing Mode)

1. Go to **Google Auth Platform → Audience** (or **OAuth consent screen**).
2. Choose **External** and leave the publishing status in **Testing** mode (do **not** publish to Production — Testing mode exempts personal apps from Google OAuth CASA verification).
3. Under **Test users**, add the Google account linked to your Pixel Watch 2 / Google Health.
4. Under **Data Access / Scopes**, add:
   - `https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly`

### 3. Create OAuth 2.0 Credentials

1. Go to **Clients → Create Client**.
2. Choose **Web application** (or **Desktop app**).
3. If using Web application, add **Authorized redirect URI**: `http://127.0.0.1:8765/callback`.
4. Copy the **Client ID** and **Client Secret** (or download the JSON file).

### 4. Initialize Local Credentials

```bash
python3 scripts/training/sync_google_health.py init
```

Edit `~/.config/google-health-sync/config.json` and paste your `client_id` and `client_secret` (or overwrite it with the JSON downloaded from Google Cloud Console — both formats are supported).

### 5. Authenticate (OAuth 2.0 + PKCE)

```bash
python3 scripts/training/sync_google_health.py auth
```

This opens your browser to Google's consent screen, captures the callback locally on `127.0.0.1:8765`, and saves your tokens to `~/.config/google-health-sync/tokens.json`.

> **Note:** In Google Cloud Testing mode, refresh tokens expire every 7 days. When a token expires, simply re-run `auth` (takes ~5 seconds in the browser).

## Daily / Weekly Usage

Preview what will be imported (safe dry run):

```bash
python3 scripts/training/sync_google_health.py sync --days 30 --dry-run
```

Import new swim and gym sessions into `Training/Logs/`:

```bash
python3 scripts/training/sync_google_health.py sync --days 30
```

Backfill from a specific date:

```bash
python3 scripts/training/sync_google_health.py sync --after 2026-01-01
```

## Notes on Idempotency

- Every imported note records its `Google Health ID`.
- Re-running `sync` scans `Training/Logs/` and skips any already-imported session, so manual edits (main set details, gym exercises, shoulder/recovery notes) are never overwritten.
