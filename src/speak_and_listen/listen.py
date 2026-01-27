import speech_recognition as sr
from speak_and_listen.speak import speak
import random
import time

listening_messages = [
    "I'm listening ...",
    "What is it?",
    "Tell me",
    "Yes?",
    "Go ahead",
    "I'm here ..."
]

def take_command(again_asked=False):
    r = sr.Recognizer()

    if(again_asked):
        pass
    else:
        speak(random.choice(listening_messages))
        time.sleep(0.5)

    with sr.Microphone(device_index=4, sample_rate=44100, chunk_size=1024) as source:

        try:
            print("Listening...")
            r.dynamic_energy_threshold = False
            r.energy_threshold = 400
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=7)

            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
            return query.lower()

        except sr.WaitTimeoutError:
            print("Maya: (Silence) No speech detected within timeout.")
            return ""
        
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down (Check Internet).")
            return ""
        except Exception as e:
            speak(f"Error: {e}")
            return ""
            