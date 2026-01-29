import time
import random
from speak_and_listen.listen import take_command
from speak_and_listen.speak import speak
from brain.short_memory import get_gemini_response
from .local_commands import handle_local_command
from .system_commands import handle_system_command

def process_command(command):
    local_response = handle_local_command(command)
    if local_response and local_response != "Command not found":
        return local_response

    system_response = handle_system_command(command)
    if system_response and "identify" not in system_response: 
        return system_response

    action_prefixes = ["open", "kill", "say", "switch", "play", "update", "shutdown", "close"]
    if any(command.lower().startswith(p) for p in action_prefixes):
        return "I found the action, but I don't know how to handle this command yet."

    print(f"Asking Gemini for: {command} ...")
    return get_gemini_response(command)

def commands():
    command = take_command()
    
    if command == "none" or command == "":
        return

    if command:
        response = process_command(command)
        if response:
            speak(response)