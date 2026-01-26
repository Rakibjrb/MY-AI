import time
from speak_and_listen.speak import speak
from local_functions.saytime import saytime, wish_me

def startup():
    print("System is starting up please wait for a while...")
    time.sleep(5)
    speak("System is online...")
    saytime()
    wish_me()