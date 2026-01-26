import time
from speak_and_listen.speak import speak
from local_functions.startup import startup
from speak_and_listen.wake import listen_wake_word
from handle.local_commands import commands

def main_system():
    try:
        startup() # System startup
        commands()
        while True:
            if listen_wake_word():
                commands()
            
    except Exception as e:
        speak(f"System Error: {e}") # System error

if __name__ == "__main__":
    main_system()