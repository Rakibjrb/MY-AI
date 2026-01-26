import time
from speak_and_listen.wake import listen_wake_word
from speak_and_listen.listen import take_command
from speak_and_listen.speak import speak
from local_functions.saytime import saytime
from local_functions.saytime import wish_me

def commands():
    if listen_wake_word():
        command = take_command()
        if "who are you" in command:
            speak("I am Maya, your personal AI assistant. Optimized by Rakibul.")
        elif "time" in command:
            saytime()
        elif "date" in command:
            speak(time.strftime("%d %B, %Y"))
        elif "day" in command:
            speak(time.strftime("%A"))
        elif "wish me" in command:
            wish_me()