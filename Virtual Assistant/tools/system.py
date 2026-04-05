import os
from output.voice import speak


def shutdown(delay: int = 5) -> None:
    speak(f"Shutting down in {delay} seconds.")
    os.system(f"shutdown /s /t {delay}")


def restart(delay: int = 5) -> None:
    speak(f"Restarting in {delay} seconds.")
    os.system(f"shutdown /r /t {delay}")


def cancel_shutdown() -> None:
    """Abort a pending shutdown or restart."""
    os.system("shutdown /a")
    speak("Shutdown cancelled.")