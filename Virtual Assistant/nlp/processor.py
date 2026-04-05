from nlp.normalizer import normalize, extract_after

from tools.app_control import open_item, close_app
from tools.window_control import (
    minimize, maximize, restore,
    close_window, switch_app, show_desktop,
    snap_left, snap_right,
)
from tools.browser import (
    new_tab, close_tab, next_tab,
    previous_tab, reopen_tab,
    refresh, hard_refresh,
    go_back, go_forward,
)
from tools.media import play_song
from tools.system import shutdown, restart
from tools.news import get_news
from output.voice import speak


# ── Intent map ────────────────────────────────────────────────────────────────
# Each entry: (match_fn, handler)
# match_fn receives the normalised command string → bool
# handler receives the normalised command string → None
#
# Rules evaluated top-to-bottom; first match wins.
# Place more specific patterns ABOVE general ones.

def _starts(prefix: str):
    return lambda c: c.startswith(prefix)

def _contains(*keywords: str):
    return lambda c: any(k in c for k in keywords)


INTENT_MAP = [
    # ── Multi-command passthrough ─────────────────────────────────────────────
    # Handled in process_command() before the map is reached.

    # ── App control ──────────────────────────────────────────────────────────
    (_starts("open "),  lambda c: open_item(extract_after(c, "open"))),
    (_starts("close "), lambda c: close_app(extract_after(c, "close"))),

    # ── Browser ──────────────────────────────────────────────────────────────
    (_contains("new tab"),                  lambda _: new_tab()),
    (_contains("close tab"),                lambda _: close_tab()),
    (_contains("reopen tab", "restore tab"),lambda _: reopen_tab()),
    (_contains("next tab"),                 lambda _: next_tab()),
    (_contains("previous tab", "back tab"), lambda _: previous_tab()),
    (_contains("hard refresh"),             lambda _: hard_refresh()),
    (_contains("refresh"),                  lambda _: refresh()),
    (_contains("go back", "browser back"),  lambda _: go_back()),
    (_contains("go forward"),               lambda _: go_forward()),

    # ── Window control ───────────────────────────────────────────────────────
    (_starts("minimize"), lambda c: minimize(extract_after(c, "minimize") or None)),
    (_starts("minimise"), lambda c: minimize(extract_after(c, "minimise") or None)),
    (_starts("maximize"), lambda c: maximize(extract_after(c, "maximize") or None)),
    (_starts("maximise"), lambda c: maximize(extract_after(c, "maximise") or None)),
    (_starts("restore"),  lambda c: restore(extract_after(c, "restore") or None)),
    (_contains("close window"),             lambda _: close_window()),
    (_contains("switch app", "switch window", "alt tab"), lambda _: switch_app()),
    (_contains("show desktop", "desktop"),  lambda _: show_desktop()),
    (_contains("snap left"),                lambda _: snap_left()),
    (_contains("snap right"),               lambda _: snap_right()),

    # ── Media ────────────────────────────────────────────────────────────────
    (_starts("play "), lambda c: play_song(extract_after(c, "play"))),

    # ── News ─────────────────────────────────────────────────────────────────
    (_contains("news", "headlines"),        lambda _: get_news()),

    # ── System ───────────────────────────────────────────────────────────────
    (_contains("shutdown", "shut down"),    lambda _: shutdown()),
    (_contains("restart", "reboot"),        lambda _: restart()),
]


# ── Router ────────────────────────────────────────────────────────────────────
def process_command(command: str) -> None:
    """
    Normalise → split multi-commands → match intent → dispatch handler.
    """
    c = normalize(command)
    print(f"[CMD] {c}")

    # Multi-command: "open chrome and play lofi"
    if " and " in c:
        for part in c.split(" and "):
            process_command(part.strip())
        return

    for match_fn, handler in INTENT_MAP:
        if match_fn(c):
            handler(c)
            return

    speak("I didn't understand that. Please try again.")