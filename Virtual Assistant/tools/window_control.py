import pyautogui
import pygetwindow as gw
from output.voice import speak


def _find_window(app_name: str):
    try:
        windows = [w for w in gw.getWindowsWithTitle(app_name) if w.isVisible]
        return windows[0] if windows else None
    except Exception as e:
        print(f"[ERROR] Window search: {e}")
        return None


def minimize(app_name: str | None = None) -> None:
    try:
        if app_name:
            win = _find_window(app_name)
            if win:
                win.minimize()
                speak(f"Minimized {app_name}")
                return
        pyautogui.hotkey("win", "down")
        speak("Window minimized")
    except Exception as e:
        print(f"[ERROR] Minimize: {e}")
        speak("Couldn't minimize")


def maximize(app_name: str | None = None) -> None:
    try:
        if app_name:
            win = _find_window(app_name)
            if win:
                if not win.isMaximized:
                    win.maximize()
                speak(f"Maximized {app_name}")
                return
        pyautogui.hotkey("win", "up")
        speak("Window maximized")
    except Exception as e:
        print(f"[ERROR] Maximize: {e}")
        speak("Couldn't maximize")


def restore(app_name: str | None = None) -> None:
    try:
        if app_name:
            win = _find_window(app_name)
            if win:
                win.restore()
                speak(f"Restored {app_name}")
                return
        pyautogui.hotkey("win", "shift", "up")
        speak("Window restored")
    except Exception as e:
        print(f"[ERROR] Restore: {e}")
        speak("Couldn't restore")


def close_window(app_name: str | None = None) -> None:
    try:
        if app_name:
            win = _find_window(app_name)
            if win:
                win.activate()
        pyautogui.hotkey("alt", "f4")
        speak("Window closed")
    except Exception as e:
        print(f"[ERROR] Close window: {e}")
        speak("Couldn't close window")


def switch_app() -> None:
    try:
        pyautogui.hotkey("alt", "tab")
        speak("Switched app")
    except Exception as e:
        print(f"[ERROR] Switch app: {e}")


def show_desktop() -> None:
    try:
        pyautogui.hotkey("win", "d")
        speak("Showing desktop")
    except Exception as e:
        print(f"[ERROR] Show desktop: {e}")


def snap_left() -> None:
    try:
        pyautogui.hotkey("win", "left")
        speak("Snapped left")
    except Exception as e:
        print(f"[ERROR] Snap left: {e}")


def snap_right() -> None:
    try:
        pyautogui.hotkey("win", "right")
        speak("Snapped right")
    except Exception as e:
        print(f"[ERROR] Snap right: {e}")