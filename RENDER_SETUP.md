# Falcony Bot — Render deployment starter

This ZIP is prepared for a Render **Web Service** (the bot starts a small Flask health page as well).
It is not a guarantee that every legacy feature/API still works; the source has not been fully runtime-tested.

## Render settings
- Runtime: Python
- Build command: `pip install -r requirements.txt`
- Start command: `python CodeX.py`

## Environment variables
Add these under Render → Environment (do not commit secrets to GitHub):
- `TOKEN` — Discord bot token (required)
- `OWNER_IDS` — your Discord user ID(s), comma-separated (required to enable owner-only commands)
- `COMMAND_LOG_WEBHOOK` — optional command log webhook
- `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` — optional music Spotify integration
- `GIPHY_API_KEY` — optional GIF integration
- `GROQ_API_KEY` — optional AI feature key

The included `.env.example` is a template only. Render should use its Environment settings.

## Important notes
1. Use Python 3.11 as the source README requests.
2. This code has many cogs and a large dependency list. Some old packages or third-party APIs may have changed; check Render build logs if installation fails.
3. The AI configuration uses an older model name in `config.yml`; AI chat may need a currently supported Groq model configured before it works.
4. The bot uses SQLite files in `db/`. Render's normal filesystem is ephemeral; attach a persistent disk and store the database directory on it if you need data to survive redeploys/restarts. This starter does not automatically migrate the DB directory.
5. The original archive contained hardcoded command-log, Spotify, and Giphy credentials. Those literals have been replaced with environment variables in this starter. Revoke/rotate any original credentials if that ZIP was shared.
6. Review permissions and commands before inviting the bot. Do not give it Administrator unless the features genuinely require it.

## Branding and emoji fallback
- Bot branding text has been changed to **Falcony**.
- Custom server-only emoji codes have been replaced with standard Unicode emoji so they display without requiring the original emoji server.
