from rapidfuzz import process, fuzz

def handle_system_command(command):
    command = command.lower().strip()
    devices = ["light", "fan", "ac", "water pump"]
    actions = ["switch on", "switch off", "turn on", "turn off", "start", "stop"]
    device_match = process.extractOne(command, devices, scorer=fuzz.partial_ratio)
    action_match = process.extractOne(command, actions, scorer=fuzz.partial_ratio)

    if device_match and device_match[1] >= 70:
        found_device = device_match[0]
        
        if action_match and action_match[1] >= 70:
            found_action = action_match[0]
            
            if any(word in found_action for word in ["on", "start"]):
                status = "ON"
                # send command to hardware
            else:
                status = "OFF"
                # send command to hardware
            
            return f"Switching {status} the {found_device}. Completed!"

    return "Sorry Rakibul, I couldn't identify the device or the action."