import time
import random
from speak_and_listen.listen import take_command
from speak_and_listen.speak import speak
from brain.short_memory import get_gemini_response
from .local_commands import handle_local_command
from .system_commands import handle_system_command

def process_command(command):
    local_response = handle_local_command(command)
    if local_response:
        return local_response

    system_response = handle_system_command(command)
    if system_response:
        return system_response

    if any(command.startswith(prefix) for prefix in ["open", "kill", "say", "switch", "play", "update"]):
        return "command not found"
    
    if not local_response and not system_response:
        print(f"Generating response for: {command} ...")
        return get_gemini_response(command)

def commands():
    command = take_command()
    
    if command == "none" or command == "":
        return

    if command:
        response = process_command(command)
        if response:
            speak(response)