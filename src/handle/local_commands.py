import time
import random
from speak_and_listen.listen import take_command
from speak_and_listen.speak import speak
from local_functions.saytime import saytime
from local_functions.saytime import wish_me
from brain.short_memory import get_gemini_response

def ask_again():
    confirm_command = ["yes", "sure", "have"]
    random_speak = ["Anything else?", "Do you have any other questions?"]
    speak(random.choice(random_speak))
    command = take_command(again_asked=True)
    print(f"from ask_again: {command}")
    if any(confirm in command for confirm in confirm_command):
        commands()
    elif "" in command:
        speak("Ok, ask me anything anytime I will be here.")
    else:
        pass

def commands():
    command = take_command()
    
    if command == "none" or command == "":
        return

    # local system commands
    if "time" in command:
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
        
    # generate response from gemini
    else:
        print(f"Thinking about: {command} ...")
        response = get_gemini_response(command)
        speak(response)
        ask_again()