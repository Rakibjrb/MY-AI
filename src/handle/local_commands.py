import time
import os
from local_functions.saytime import saytime
import subprocess
from speak_and_listen.speak import speak
from speak_and_listen.listen import take_command

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
    elif "open code editor" in received or "open editor" in received or "open workspace" in received:
        return handle_apps("antigravity")
    elif "kill chrome" in received or "close chrome" in received:
        return handle_kill("chrome")
    elif "kill brave" in received or "close brave" in received:
        return handle_kill("brave")
    elif "kill code editor" in received or "close code editor" in received or "close workspace" in received:
        return handle_kill("antigravity")
    elif "update operating system" in received or "update os" in received:
        speak("Updating operating system")
        os.system("sudo apt update && sudo apt upgrade -y")
        return "Operating system updated successfully"
    elif any(received.startswith(shutdown) for shutdown in ["shutdown operating system now", "shutdown the system now", "shutdown", "shutdown pc", "shutdown the pc now"]):
        speak("Please Confirm again, Should I shutdown the operating system?")
        confirm_command = take_command(with_response=False)
        if any(confirm_command.startswith(confirm) for confirm in ["yes", "shut down", "shutdown", "yes shutdown", "shutdown", "shutdown now", "sure", "sure shutdown", "sure shutdown now"]):
            speak("Confirmed, shutting down the operating system")
            speak("3")
            speak("2")
            speak("1")
            os.system("poweroff")
        else:
            return "Ok I will not shutdown the operating system"