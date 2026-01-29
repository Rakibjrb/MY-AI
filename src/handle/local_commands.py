import time
import os
import subprocess
from rapidfuzz import process, fuzz
from local_functions.saytime import saytime
from speak_and_listen.speak import speak
from speak_and_listen.listen import take_command

commands_map = {
    "say time": "time",
    "say date": "date",
    "say day": "day",
    "play music": "music",
    "open youtube": "youtube",
    "open whatsapp": "whatsapp",
    "open chatgpt": "chatgpt",
    "open gemini": "gemini",
    "open figma": "figma",
    "open course": "course",
    "open github": "github",
    "open code editor": "editor",
    "kill chrome": "close chrome",
    "kill brave": "close brave",
    "update os": "update",
    "shutdown": "shutdown"
}

def open_browser(app, url):
    subprocess.Popen([app, "--new-window", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def handle_apps(app):
    subprocess.Popen([app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return f"{app} opened"

def handle_kill(app):
    os.system(f"pkill {app}")
    return f"{app} closed"

def handle_local_command(received):
    received = received.lower().strip()
    
    all_keys = list(commands_map.keys())
    matched = process.extractOne(received, all_keys, scorer=fuzz.partial_ratio)
    
    best_match = ""
    if matched and matched[1] >= 70:
        best_match = matched[0]
        print(f"Best match: {best_match} ({matched[1]}%)")

    if best_match == "say time" or "time" in received:
        return f"The time is {saytime()}"

    elif best_match == "say date" or "date" in received:
        return f"The date is {time.strftime('%d %B, %Y')}"

    elif best_match == "say day" or "day" in received:
        return f"The day is {time.strftime('%A')}"

    elif best_match == "play music" or "music" in received:
        open_browser("brave-browser", "https://www.youtube.com/watch?v=FPWO8dqY0v0&list=PLx5WzpveccBxCVltNCKvP9hGCTk1-Zhrh&index=0")
        time.sleep(1)
        os.system("pactl set-sink-volume @DEFAULT_SINK@ 80%")
        return "playing music"

    elif best_match == "open youtube" or "youtube" in received:
        open_browser("google-chrome", "https://www.youtube.com/")
        return "youtube opened"

    elif best_match == "open whatsapp" or "whatsapp" in received:
        open_browser("google-chrome", "https://web.whatsapp.com/")
        return "whatsapp opened check your messages"

    elif best_match == "open chatgpt" or "chatgpt" in received:
        open_browser("google-chrome", "https://chatgpt.com/")
        return "chatgpt opened"

    elif best_match == "open gemini" or "gemini" in received:
        open_browser("google-chrome", "https://gemini.google.com/app")
        return "gemini opened"

    elif best_match == "open figma" or "figma" in received:
        open_browser("google-chrome", "https://www.figma.com/")
        return "figma opened"

    elif best_match == "open course" or "course" in received:
        open_browser("google-chrome", "https://web.programming-hero.com/dashboard")
        return "course opened learn effectively"

    elif best_match == "open github" or "github" in received:
        open_browser("google-chrome", "https://github.com/rakibjrb")
        return "github profile opened"
    
    elif best_match == "open code editor" or "editor" in received:
        return handle_apps("antigravity")

    elif "kill" in best_match or "close" in received:
        if "chrome" in received: return handle_kill("chrome")
        if "brave" in received: return handle_kill("brave")
        if "editor" in received: return handle_kill("antigravity")

    elif "update system" in received or "update os" in received:
        speak("Updating operating system")
        os.system("sudo apt update && sudo apt upgrade -y")
        return "Operating system updated successfully"

    elif any(word in received for word in ["shutdown", "power off", "turn off"]):
        if fuzz.partial_ratio("shutdown", received) > 80:
            speak("Please Confirm again, Should I shutdown the operating system?")
            time.sleep(1)
            os.system("pactl set-sink-mute @DEFAULT_SINK@ 1") 
            confirm_command = take_command(with_response=False).lower()
            os.system("pactl set-sink-mute @DEFAULT_SINK@ 0") 
            
            yes_score = fuzz.partial_ratio("yes", confirm_command)
            sure_score = fuzz.partial_ratio("sure", confirm_command)
            
            if max(yes_score, sure_score) > 80 or "shut" in confirm_command:
                speak("Confirmed, shutting down the operating system")
                for i in range(3, 0, -1):
                    speak(str(i))
                    time.sleep(0.5)
                os.system("poweroff")
            else:
                return "Ok Rakibul, I will not shutdown the operating system"
    
    return "Command not found"