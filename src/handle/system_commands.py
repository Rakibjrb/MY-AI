def handle_system_command(command):
    devices = ["light", "fan", "ac", "water pump"]
    
    for device in devices:
        if device in command:
            if "on" in command:
                return f"Switching ON the {device}. Completed!"
            elif "off" in command:
                return f"Switching OFF the {device}. Completed!"