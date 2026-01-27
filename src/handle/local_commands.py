import time
from speak_and_listen.listen import take_command
from speak_and_listen.speak import speak
from local_functions.saytime import saytime
from local_functions.saytime import wish_me

def ask_again():
    confirm_command = ["yes", "sure", "have"]
    speak("Do you have any other questions?")
    command = take_command(again_asked=True)
    print(f"from ask_again: {command}")
    if any(confirm in command for confirm in confirm_command):
        commands()
    else:
        speak("Ok, ask me anything anytime I will be here.")

def commands():
    command = take_command()
    if "who are you" in command:
        speak("I am Maya, A personal AI voice assistant")
        ask_again()
    elif "hi" in command or "hello" in command:
        speak("Hello! How can I help you today?")
        ask_again()
    elif "how are you" in command:
        speak("I am fine, thank you! How about you?")
        ask_again()
    elif "time" in command:
        speak(f"The time is {saytime()}")
        ask_again()
    elif "date" in command:
        speak(time.strftime("%d %B, %Y"))
        ask_again()
    elif "day" in command:
        speak(time.strftime("%A"))
        ask_again()
    elif "wish me" in command:
        wish_me()
        ask_again()
    elif "exit" in command or "quit" in command or "shutdown" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        return