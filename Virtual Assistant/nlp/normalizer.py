import re

# ── Phrase normalisation map ───────────────────────────────────────────────────
# Order matters: longer phrases first to avoid partial replacements
REPLACEMENTS: dict[str, str] = {
    "turn off":        "shutdown",
    "power off":       "shutdown",
    "increase volume": "volume up",
    "decrease volume": "volume down",
    "launch":          "open",
    "start":           "open",
    "run":             "open",
    "exit":            "close",
    "quit":            "close",
}

# ── Stopwords ────────────────────────────────────────────────────────────────
STOPWORDS: list[str] = [
    "please", "can you", "could you",
    "would you", "for me",
    # articles removed carefully to avoid breaking compound names
]


# ── Pipeline ─────────────────────────────────────────────────────────────────
def normalize(text: str) -> str:
    """
    Lowercase → replace synonyms → strip stopwords → collapse whitespace.
    """
    text = text.lower().strip()

    for src, dst in REPLACEMENTS.items():
        text = text.replace(src, dst)

    for word in STOPWORDS:
        # Whole-phrase removal with surrounding space guards
        text = re.sub(rf"\b{re.escape(word)}\b", "", text)

    return re.sub(r"\s+", " ", text).strip()


def extract_after(command: str, keyword: str) -> str:
    """
    Returns everything after the first occurrence of keyword.
    Example: extract_after("open visual studio code", "open") → "visual studio code"
    """
    idx = command.find(keyword)
    if idx == -1:
        return command
    return command[idx + len(keyword):].strip()