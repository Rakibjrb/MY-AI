import os
import subprocess
from gtts import gTTS
from langdetect import detect

def speak(text):
    main_voice = "maya.mp3"
    detected_lang = 'en'

    try:
        try:
            detected_lang = detect(text) # detect language
        except:
            detected_lang = 'en' # default language is english
        
        print(f"Maya Speaking ...")
        tts = gTTS(text=text, lang=detected_lang, slow=False)
        tts.save(main_voice)

        subprocess.run(["mpg123", "-q", main_voice])

    except Exception as e:
        print(f"Error on Voice System: {e}")
        tts = gTTS(text="Error on Voice System", lang="en", slow=False)
        tts.save(main_voice)

        subprocess.run(["mpg123", "-q", main_voice])
    
    finally:
        if os.path.exists(main_voice):
            os.remove(main_voice)