import time
from local_functions.saytime import saytime

def handle_local_command(received_command):
    if "say time" in received_command:
        return f"The time is {saytime()}"
    elif "say date" in received_command:
        return f"The date is {time.strftime('%d %B, %Y')}"
    elif "say day" in received_command:
        return f"The day is {time.strftime('%A')}"
    elif "shutdown" in received_command:
        return "Shutting down the system. Goodbye! Have a great day!"
        exit()