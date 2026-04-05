import os
import subprocess
import webbrowser
from output.voice import speak

SYSTEM_APPS = {
    "control panel": "control",
    "task manager": "taskmgr",
    "file explorer": "explorer",
    "command prompt": "cmd",
    "powershell": "powershell",
    "calculator": "calc",
    "notepad": "notepad",
    "paint": "mspaint",
    "wordpad": "write",
    "character map": "charmap",
    "device manager": "devmgmt.msc",
    "disk management": "diskmgmt.msc",
    "services": "services.msc",
    "event viewer": "eventvwr",
    "system configuration": "msconfig",
    "registry editor": "regedit",
    "computer management": "compmgmt.msc",
    "windows features": "optionalfeatures",
    "programs and features": "appwiz.cpl",
    "network connections": "ncpa.cpl",
    "power options": "powercfg.cpl",
    "sound settings": "mmsys.cpl",
    "display settings": "desk.cpl",
    "mouse settings": "main.cpl",
    "keyboard settings": "control keyboard",
    "date and time": "timedate.cpl",
    "region settings": "intl.cpl",
    "user accounts": "netplwiz",
    "windows security": "windowsdefender:",
    "printer settings": "control printers",
    "bluetooth settings": "fsquirt",
    "windows update": "ms-settings:windowsupdate",
    "settings": "ms-settings:",
    "run dialog": "winver",
    "system information": "msinfo32",
    "resource monitor": "resmon",
    "performance monitor": "perfmon",
    "clipboard": "win+v",
    "magnifier": "magnify",
    "narrator": "narrator",
    "on-screen keyboard": "osk",
    "windows media player": "wmplayer",
    "sound recorder": "soundrecorder",
    "sticky notes": "stikynot",
    "snipping tool": "snippingtool",
    "xbox game bar": "gamebar",
    "camera": "microsoft.windows.camera:",
    "photos": "ms-photos:",
    "calendar": "outlookcal:",
    "mail": "outlookmail:",
    "store": "ms-windows-store:",
    "weather": "msnweather:",
    "news": "msnnews:",
    "sports": "msnsports:",
    "money": "msnmoney:",
    "travel": "msntravel:"
}

# === Regular Apps Dictionary ===
APPS = {
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "firefox": "firefox.exe",
    "opera": "opera.exe",
    "code": "code.exe",
    "visual studio": "devenv.exe",
    "pycharm": "pycharm64.exe",
    "intellij": "idea64.exe",
    "android studio": "studio64.exe",
    "eclipse": "eclipse.exe",
    "netbeans": "netbeans64.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "outlook": "outlook.exe",
    "onenote": "onenote.exe",
    "access": "msaccess.exe",
    "publisher": "mspub.exe",
    "visio": "visio.exe",
    "project": "winproj.exe",
    "teams": "teams.exe",
    "skype": "skype.exe",
    "zoom": "zoom.exe",
    "discord": "discord.exe",
    "slack": "slack.exe",
    "whatsapp": "whatsapp.exe",
    "telegram": "telegram.exe",
    "vscode": "code.exe",
    "notepad": "notepad++.exe",
    "sublime": "sublime_text.exe",
    "atom": "atom.exe",
    "photoshop": "photoshop.exe",
    "illustrator": "illustrator.exe",
    "premiere": "premiere.exe",
    "after effects": "afterfx.exe",
    "lightroom": "lightroom.exe",
    "acrobat": "acrobat.exe",
    "reader": "acrord32.exe",
    "winrar": "winrar.exe",
    "7zip": "7zfm.exe",
    "winzip": "winzip64.exe",
    "spotify": "spotify.exe",
    "vlc": "vlc.exe",
    "media player": "wmplayer.exe",
    "quicktime": "quicktimeplayer.exe",
    "itunes": "itunes.exe",
    "steam": "steam.exe",
    "epic games": "epicgameslauncher.exe",
    "origin": "origin.exe",
    "battle.net": "battle.net.exe",
    "utorrent": "utorrent.exe",
    "bittorrent": "bittorrent.exe",
    "qbittorrent": "qbittorrent.exe",
    "teamviewer": "teamviewer.exe",
    "anydesk": "anydesk.exe",
    "ccleaner": "ccleaner64.exe",
    "malwarebytes": "mbam.exe",
    "avast": "avastui.exe",
    "avg": "avgui.exe",
    "norton": "norton.exe",
    "kaspersky": "avp.exe",
    "python": "python.exe",
    "java": "javaw.exe",
    "node": "node.exe",
    "git": "git-bash.exe",
    "docker": "docker.exe",
    "postman": "postman.exe",
    "mysql": "mysql.exe",
    "workbench": "mysqlworkbench.exe",
    "mongodb": "mongodb.exe",
    "redis": "redis-server.exe",
    "virtualbox": "virtualbox.exe",
    "vmware": "vmware.exe",
    "hyper-v": "vmconnect.exe",
    "blender": "blender.exe",
    "maya": "maya.exe",
    "3ds max": "3dsmax.exe",
    "cinema 4d": "cinema4d.exe",
    "unity": "unity.exe",
    "unreal": "unrealengine.exe",
    "godot": "godot.exe",
    "obs": "obs64.exe",
    "streamlabs": "streamlabs.exe",
    "xsplit": "xsplit.exe",
    "camtasia": "camtasia.exe",
    "audacity": "audacity.exe",
    "gimp": "gimp-2.10.exe",
    "inkscape": "inkscape.exe",
    "krita": "krita.exe",
    "lightshot": "lightshot.exe",
    "sharex": "sharex.exe",
    "greenshot": "greenshot.exe",
    "onenote": "onenote.exe",
    "evernote": "evernote.exe",
    "notion": "notion.exe",
    "todoist": "todoist.exe",
    "trello": "trello.exe",
    "asana": "asana.exe",
    "clickup": "clickup.exe"
}

# === Websites Dictionary ===
SITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://www.github.com",
    "stackoverflow": "https://stackoverflow.com",
    "reddit": "https://www.reddit.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://www.spotify.com",
    "gmail": "https://mail.google.com",
    "outlook": "https://outlook.live.com",
    "drive": "https://drive.google.com",
    "dropbox": "https://www.dropbox.com",
    "whatsapp": "https://web.whatsapp.com",
    "telegram": "https://web.telegram.org",
    "discord": "https://discord.com",
    "twitch": "https://www.twitch.tv",
    "microsoft": "https://www.microsoft.com",
    "apple": "https://www.apple.com",
    "ubuntu": "https://ubuntu.com",
    "wordpress": "https://wordpress.com",
    "medium": "https://medium.com",
    "quora": "https://www.quora.com",
    "pinterest": "https://www.pinterest.com",
    "tumblr": "https://www.tumblr.com",
    "flickr": "https://www.flickr.com",
    "imgur": "https://imgur.com",
    "unsplash": "https://unsplash.com",
    "deviantart": "https://www.deviantart.com",
    "behance": "https://www.behance.net",
    "dribbble": "https://dribbble.com",
    "figma": "https://www.figma.com",
    "canva": "https://www.canva.com",
    "notion": "https://www.notion.so",
    "trello": "https://trello.com",
    "asana": "https://asana.com",
    "slack": "https://slack.com",
    "zoom": "https://zoom.us",
    "teams": "https://teams.microsoft.com",
    "skype": "https://web.skype.com",
    "signal": "https://signal.org",
    "paypal": "https://www.paypal.com",
    "stripe": "https://stripe.com",
    "coinbase": "https://www.coinbase.com",
    "binance": "https://www.binance.com",
    "kraken": "https://www.kraken.com",
    "booking": "https://www.booking.com",
    "airbnb": "https://www.airbnb.com",
    "tripadvisor": "https://www.tripadvisor.com",
    "expedia": "https://www.expedia.com",
    "kayak": "https://www.kayak.com",
    "uber": "https://www.uber.com",
    "lyft": "https://www.lyft.com",
    "doordash": "https://www.doordash.com",
    "ubereats": "https://www.ubereats.com",
    "grubhub": "https://www.grubhub.com",
    "yelp": "https://www.yelp.com",
    "zillow": "https://www.zillow.com",
    "realtor": "https://www.realtor.com",
    "indeed": "https://www.indeed.com",
    "glassdoor": "https://www.glassdoor.com",
    "monster": "https://www.monster.com",
    "craigslist": "https://craigslist.org",
    "ebay": "https://www.ebay.com",
    "etsy": "https://www.etsy.com",
    "walmart": "https://www.walmart.com",
    "target": "https://www.target.com",
    "bestbuy": "https://www.bestbuy.com",
    "homedepot": "https://www.homedepot.com",
    "lowes": "https://www.lowes.com",
    "ikea": "https://www.ikea.com",
    "wayfair": "https://www.wayfair.com",
    "overstock": "https://www.overstock.com"
}
def _find_match(name: str, registry: dict[str, str]) -> tuple[str, str] | None:
    """
    Returns (key, value) for best match in registry.
    Exact match takes priority over partial match.
    """
    if name in registry:
        return name, registry[name]
    # Partial: name is a substring of a key
    for key, val in registry.items():
        if name in key:
            return key, val
    return None
 
 
def _open_system_app(command: str, label: str) -> None:
    speak(f"Opening {label}")
    try:
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"[ERROR] System app: {e}")
        speak(f"Couldn't open {label}")
 
 
def _open_app(exe: str, label: str) -> None:
    speak(f"Opening {label}")
    try:
        os.system(f'start "" "{exe}"')
    except Exception as e:
        print(f"[ERROR] App: {e}")
        speak(f"Couldn't open {label}")
 
 
def _open_site(url: str, label: str) -> None:
    speak(f"Opening {label}")
    webbrowser.open(url)
 
 
# ── Public API ───────────────────────────────────────────────────────────────
 
def open_item(name: str) -> None:
    name = name.lower().strip()
    print(f"[Open] {name}")
 
    # Priority: system apps → installed apps → websites
    match = _find_match(name, SYSTEM_APPS)
    if match:
        _open_system_app(match[1], match[0])
        return
 
    match = _find_match(name, APPS)
    if match:
        _open_app(match[1], match[0])
        return
 
    match = _find_match(name, SITES)
    if match:
        _open_site(match[1], match[0])
        return
 
    speak(f"Sorry, I couldn't find {name}.")
 
 
def close_app(name: str) -> None:
    name = name.lower().strip()
    print(f"[Close] {name}")
 
    match = _find_match(name, APPS)
    if match:
        label, exe = match
        speak(f"Closing {label}")
        result = os.system(f"taskkill /IM {exe} /F >nul 2>&1")
        if result != 0:
            speak(f"{label} doesn't appear to be running")
        return
 
    if _find_match(name, SYSTEM_APPS):
        speak(f"{name} is a system component and can't be closed this way")
        return
 
    # Last resort — try name.exe directly
    speak(f"Attempting to close {name}")
    os.system(f"taskkill /IM {name}.exe /F >nul 2>&1")
 