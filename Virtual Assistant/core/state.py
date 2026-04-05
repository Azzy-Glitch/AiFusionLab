import threading

# ── Wakeword / command state ──────────────────────────────────────────────────
awake: bool = False          # True after wake word detected
listening: bool = True       # False to shut down the listener loop
stop_flag: bool = False      # Future use: force-stop long operations

# ── Thread reference ──────────────────────────────────────────────────────────
command_thread: threading.Thread | None = None