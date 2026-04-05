import pywhatkit
from output.voice import speak


def play_song(song: str) -> None:
    if not song:
        speak("What would you like me to play?")
        return
    speak(f"Playing {song}")
    pywhatkit.playonyt(song)