import os
import subprocess
from gtts import gTTS
from langdetect import detect

supported_languages = ['bn', 'en', 'hi', 'es', 'fr', 'de', 'ja', 'ar']

def speak(text):
    main_voice = "maya.mp3"

    try:
        try:
            detected_lang = detect(text) # detect language
        except:
            detected_lang = 'en' # default language is english
        
        final_lang = detected_lang if detected_lang in supported_languages else 'en'
        print(f"Maya Speaking in {final_lang}...")
        tts = gTTS(text=text, lang=final_lang, slow=False)
        tts.save(main_voice)

        subprocess.run(["mpg123", "-q", main_voice])

    except Exception as e:
        print(f"Error on Voice System: {e}")
        tts = gTTS(text=text, lang=final_lang, slow=False)
        tts.save(main_voice)

        subprocess.run(["mpg123", "-q", main_voice])
    
    finally:
        if os.path.exists(main_voice):
            os.remove(main_voice)