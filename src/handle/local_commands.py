import time
from speak_and_listen.listen import take_command
from speak_and_listen.speak import speak
from local_functions.saytime import saytime
from local_functions.saytime import wish_me

def ask_again():
    speak("Do you have any other questions?")
    if "yes" in take_command() or "sure" in take_command():
        commands()
    else:
        speak("Thank you for using my services. Have a great day!")

def commands():
    command = take_command()
    if "who are you" in command:
        speak("I am Maya, your personal AI assistant. Optimized by Rakibul.")
    elif "hi" in command or "hello" in command:
        speak("Hello! How can I help you today?")
    elif "how are you" in command:
        speak("I am fine, thank you! How about you?")
    elif "time" in command:
        saytime()
    elif "date" in command:
        speak(time.strftime("%d %B, %Y"))
    elif "day" in command:
        speak(time.strftime("%A"))
    elif "wish me" in command:
        wish_me()
    elif "exit" in command or "quit" in command or "bye" in command or "goodbye" in command:
        speak("Goodbye! Have a great day!")
        exit()