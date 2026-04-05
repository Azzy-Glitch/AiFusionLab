import pyautogui
import psutil
from output.voice import speak


def _is_browser_running(browser: str = "chrome") -> bool:
    for proc in psutil.process_iter(["name"]):
        try:
            if browser in proc.info["name"].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False


def _require_browser(fn):
    """Decorator: only run fn if a browser is open."""
    def wrapper(*args, **kwargs):
        if _is_browser_running():
            return fn(*args, **kwargs)
        speak("No browser is open")
    return wrapper


@_require_browser
def new_tab():      pyautogui.hotkey("ctrl", "t");           speak("New tab opened")

@_require_browser
def close_tab():    pyautogui.hotkey("ctrl", "w");           speak("Tab closed")

@_require_browser
def next_tab():     pyautogui.hotkey("ctrl", "tab");         speak("Next tab")

@_require_browser
def previous_tab(): pyautogui.hotkey("ctrl", "shift", "tab"); speak("Previous tab")

@_require_browser
def reopen_tab():   pyautogui.hotkey("ctrl", "shift", "t");  speak("Reopened last tab")

@_require_browser
def refresh():      pyautogui.hotkey("ctrl", "r");           speak("Refreshing")

@_require_browser
def hard_refresh(): pyautogui.hotkey("ctrl", "shift", "r");  speak("Hard refresh done")

@_require_browser
def go_back():      pyautogui.hotkey("alt", "left");         speak("Going back")

@_require_browser
def go_forward():   pyautogui.hotkey("alt", "right");        speak("Going forward")