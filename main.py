import time
from speak_and_listen.speak import speak

def startup():
    print("System is starting up please wait for a while...")
    time.sleep(5)
    print("............. 10%")
    time.sleep(1)
    print(".................. 40%")
    time.sleep(1)
    print("...................... 70%")
    time.sleep(1)
    print("......................... 100%")
    time.sleep(1)
    print("Checking voice system")
    time.sleep(1)
    speak("Voice system working")

def main_system():
    try:
        startup()
        rakibul
    except Exception as e:
        speak(f"System Error: {e}")

if __name__ == "__main__":
    main_system()