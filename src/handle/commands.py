import time
import random
from speak_and_listen.listen import take_command
from speak_and_listen.speak import speak
from brain.short_memory import get_gemini_response
from .local_commands import handle_local_command
from .system_commands import handle_system_command

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

def process_command(command):
    print(f"Processing command: {command} ...")
    local_response = handle_local_command(command)
    if local_response:
        return local_response

    system_response = handle_system_command(command)
    if system_response:
        return system_response
    else:
        print(f"Generating response for: {command} ...")
        response = get_gemini_response(command)
        speak(response)
        ask_again()

def commands():
    command = take_command()
    
    if command == "none" or command == "":
        return

    if command:
        response = process_command(command)
        if response:
            speak(response)
            ask_again()