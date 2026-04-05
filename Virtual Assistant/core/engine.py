from output.voice import speak
from input.listener import start_background_listener


def start() -> None:
    """
    Bootstrap entry point.
    Keeps engine.py thin — all logic lives in its own module.
    """
    speak("Nexus online. Say 'Nexus' to activate.")
    # Blocks until shutdown
    start_background_listener() 