import time
import threading
import speech_recognition as sr

import core.state as state
from core.config import WAKE_WORD, COOLDOWN, PHRASE_TIME_LIMIT
from nlp.processor import process_command
from output.voice import speak, stop_speaking

recognizer = sr.Recognizer()


# ── Callback ─────────────────────────────────────────────────────────────────
def _callback(recognizer: sr.Recognizer, audio: sr.AudioData) -> None:
    """
    Invoked by SpeechRecognition's background thread on every audio segment.
    Keeps voice recognition and command execution decoupled via threading.
    """
    try:
        text = recognizer.recognize_google(audio).lower().strip()
        print(f"[Heard] {text}")

    except sr.UnknownValueError:
        return   # Silence or unintelligible — not an error
    except sr.RequestError as e:
        print(f"[SR service error] {e}")
        return
    except Exception as e:
        print(f"[Listener error] {e}")
        return

    # ── Wake word detection ───────────────────────────────────────────────────
    if WAKE_WORD in text:
        stop_speaking()           # Interrupt anything currently being said
        state.awake = True
        speak("Yes sir?")
        time.sleep(COOLDOWN)
        return

    # ── Command dispatch ──────────────────────────────────────────────────────
    if state.awake:
        state.awake = False

        # Don't stack threads — wait for the previous command to finish
        if state.command_thread and state.command_thread.is_alive():
            print("[Listener] Previous command still running — queuing after it.")
            state.command_thread.join(timeout=10)

        state.command_thread = threading.Thread(
            target=process_command,
            args=(text,),
            daemon=True,          # Dies with the main process
        )
        state.command_thread.start()


# ── Entry point ───────────────────────────────────────────────────────────────
def start_background_listener() -> None:
    """
    Calibrates mic, starts background listening loop.
    Blocks until state.listening is set to False or KeyboardInterrupt.
    """
    mic = sr.Microphone()

    with mic as source:
        print("[Listener] Calibrating for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(f"[Listener] Ready. Say '{WAKE_WORD}' to activate.")

    stop_fn = recognizer.listen_in_background(
        mic, _callback, phrase_time_limit=PHRASE_TIME_LIMIT
    )

    try:
        while state.listening:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        stop_fn(wait_for_stop=False)
        print("[Listener] Stopped.")