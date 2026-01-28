import time
import os
from local_functions.saytime import saytime
import subprocess
from speak_and_listen.speak import speak

def open_browser(app, url):
    subprocess.Popen([app, "--new-window", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def handle_apps(app):
    subprocess.Popen([app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return f"{app} opened"

def handle_kill(app):
    os.system(f"pkill {app}")
    return f"{app} closed"

def handle_local_command(received):
    if "say time" in received:
        return f"The time is {saytime()}"
    elif "say date" in received:
        return f"The date is {time.strftime('%d %B, %Y')}"
    elif "say day" in received:
        return f"The day is {time.strftime('%A')}"
    elif "play music" in received or "play my music" in received or "play favorite music" in received:
        open_browser("brave-browser", "https://www.youtube.com/watch?v=FPWO8dqY0v0&list=PLx5WzpveccBxCVltNCKvP9hGCTk1-Zhrh&index=0")
        return ""
    elif "open youtube" in received:
        open_browser("google-chrome", "https://www.youtube.com")
        return "youtube opened"
    elif "open whatsapp" in received:
        open_browser("google-chrome", "https://web.whatsapp.com")
        return "whatsapp opened check your messages"
    elif "open chatgpt" in received:
        open_browser("google-chrome", "https://chatgpt.com/")
        return "chatgpt opened"
    elif "open gemini" in received:
        open_browser("google-chrome", "https://gemini.google.com/app")
        return "gemini opened"
    elif "open figma" in received:
        open_browser("google-chrome", "https://www.figma.com/")
        return "figma opened"
    elif "open course" in received:
        open_browser("google-chrome", "https://web.programming-hero.com/dashboard")
        return "course opened learn effectively"
    elif "open github profile" in received or "open github" in received:
        open_browser("google-chrome", "https://github.com/rakibjrb")
        return "github profile opened"
    elif "open code editor" in received:
        return handle_apps("antigravity")
    elif "kill chrome" in received:
        return handle_kill("chrome")
    elif "kill brave" in received:
        return handle_kill("brave")
    elif "kill code editor" in received:
        return handle_kill("antigravity")
    elif "update operating system" in received or "update os" in received:
        speak("Updating operating system")
        os.system("sudo apt update && sudo apt upgrade -y")
        return "Operating system updated successfully"