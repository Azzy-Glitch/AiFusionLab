import os
import uuid
import socket
import threading
import pygame
import pyttsx3
from gtts import gTTS

# ── Init ──────────────────────────────────────────────────────────────────────
pygame.mixer.init()

_offline_engine = pyttsx3.init()
_offline_engine.setProperty("rate", 150)
_offline_engine.setProperty("volume", 0.9)

_speak_lock = threading.Lock()   # Prevent overlapping speak() calls
_stop_event = threading.Event()  # Signal to interrupt playback


# ── Network check ─────────────────────────────────────────────────────────────
def _is_online() -> bool:
    try:
        socket.create_connection(("www.google.com", 80), timeout=2)
        return True
    except OSError:
        return False


# ── Interrupt ─────────────────────────────────────────────────────────────────
def stop_speaking():
    """Interrupt whatever is currently being spoken."""
    _stop_event.set()
    pygame.mixer.music.stop()
    _offline_engine.stop()


# ── Core speak ────────────────────────────────────────────────────────────────
def speak(text: str) -> None:
    """
    Speak text using gTTS (online) or pyttsx3 (offline).
    Thread-safe. Cleans up temp files even on error.
    """
    _stop_event.clear()
    print(f"[Nexus] {text}")

    with _speak_lock:
        if _is_online():
            _speak_online(text)
        else:
            _speak_offline(text)


def _speak_online(text: str) -> None:
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    try:
        gTTS(text=text, lang="en").save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            if _stop_event.is_set():
                pygame.mixer.music.stop()
                break
            clock.tick(10)

    except Exception as e:
        print(f"[TTS online error] {e}")
        _speak_offline(text)          # Graceful fallback

    finally:
        # Always clean up — even if an exception occurred mid-playback
        try:
            pygame.mixer.music.unload()
        except Exception:
            pass
        if os.path.exists(filename):
            os.remove(filename)


def _speak_offline(text: str) -> None:
    """
    pyttsx3 must run on the main thread on some platforms.
    We use runAndWait() here safely because speak() is already
    serialised through _speak_lock.
    """
    try:
        _offline_engine.say(text)
        _offline_engine.runAndWait()
    except Exception as e:
        print(f"[TTS offline error] {e}")