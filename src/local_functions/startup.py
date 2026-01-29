import time
from speak_and_listen.speak import speak
from .saytime import saytime, wish_me

def startup():
    print("System is starting up please wait for a while...")
    # time.sleep(5)
    speak(f"System is online on {saytime()}...")
    wish_me()