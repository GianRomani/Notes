# Fitbit / Pixel Watch 2 Training Sync

Zero-dependency Python CLI that imports swimming and gym sessions from the **Fitbit Web API** (backing Pixel Watch 2 / Google Health) into `Training/Logs/` as Obsidian markdown notes matching `Swim Log Template.md` and `Gym Log Template.md`.

> **Security:** OAuth credentials and tokens are stored strictly outside this public repository in `~/.config/fitbit-sync/` (`0600` permissions). This `scripts/` directory is excluded from the Netlify/Zola website build in `netlify.toml`.

## One-Time Setup

### 1. Register a Personal App on Fitbit

1. Visit [dev.fitbit.com/apps/new](https://dev.fitbit.com/apps/new) and sign in with the Google/Fitbit account linked to your Pixel Watch 2.
2. Fill in the form:
   - **Application Name:** e.g. `Obsidian Training Sync`
   - **Description:** Personal workout sync to Obsidian notes
   - **Application Website URL / Organization Website URL:** `https://gianfree-notes.netlify.app` (or any personal URL)
   - **Terms of Service URL / Privacy Policy URL:** same URL
   - **OAuth 2.0 Application Type:** `Personal`
   - **Redirect URL:** `http://127.0.0.1:8765/callback`
   - **Default Access Type:** `Read-Only`
3. Copy your **OAuth 2.0 Client ID** and **Client Secret**.

### 2. Initialize Local Credentials

```bash
python3 scripts/training/sync_fitbit.py init
```

Edit `~/.config/fitbit-sync/config.json` and paste your `client_id` and `client_secret`.

### 3. Authenticate (OAuth 2.0 + PKCE)

```bash
python3 scripts/training/sync_fitbit.py auth
```

This opens your browser to Fitbit's consent screen, captures the callback locally on `127.0.0.1:8765`, and saves your refreshable tokens to `~/.config/fitbit-sync/tokens.json`.

## Daily / Weekly Usage

Preview what will be imported (safe dry run):

```bash
python3 scripts/training/sync_fitbit.py sync --days 30 --dry-run
```

Import new swim and gym sessions into `Training/Logs/`:

```bash
python3 scripts/training/sync_fitbit.py sync --days 30
```

Backfill from a specific date:

```bash
python3 scripts/training/sync_fitbit.py sync --after 2026-01-01
```

## Notes on Idempotency

- Every imported note records its `Fitbit Log ID`.
- Re-running `sync` scans `Training/Logs/` and skips any already-imported session, so manual edits (main set details, gym exercises, shoulder/recovery notes) are never overwritten.
