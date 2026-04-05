import os

# ── Wake word ─────────────────────────────────────────────────────────────────
WAKE_WORD: str = "nexus"

# ── Timing ────────────────────────────────────────────────────────────────────
COOLDOWN: float = 0.3          # Seconds after wake-word before next listen
PHRASE_TIME_LIMIT: int = 6     # Max seconds per spoken phrase

# ── API Keys (prefer env vars; fall back to placeholder) ─────────────────────
NEWS_API_KEY: str = os.getenv("NEWS_API_KEY", "7ff93445a6ea436facbbf16144903512")