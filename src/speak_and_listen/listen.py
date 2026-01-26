import speech_recognition as sr
from speak_and_listen.speak import speak
import random

listening_messages = [
    "I'm listening ...",
    "What is it?",
    "Tell me",
    "Yes?",
    "Go ahead",
    "I'm all ears"
    "I'm here ..."
]

def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = False
    r.pause_threshold = 1

    speak(random.choice(listening_messages))

    with sr.Microphone(device_index=4, sample_rate=44100, chunk_size=1024) as source:

        try:
            print("Listening...")
            audio = r.record(source, duration=5)

            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
            return query.lower()
        
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down (Check Internet).")
            return ""
        except Exception as e:
            speak(f"Error: {e}")
            return ""
            