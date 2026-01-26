import os
from gtts import gTTS
import subprocess

def speak(text, language="en"):
    main_voice="maya.mp3" # original gTTS voice
    print(f"Maya: {text}") # print text

    try:
        tts = gTTS(text=text, lang=language) # gTTS voice
        tts.save(main_voice) # save gTTS voice
        os.system(f"mpg123 -q {main_voice}") # play gTTS voice
       
    except Exception as e:
        print(f"Error on Voice System: {e}")
        errorVoice = gTTS(text=f"Error on Voice System {e}", lang="en")
        errorVoice.save("error.mp3")
        os.system("mpg123 -q error.mp3")

    finally:
        if os.path.exists(main_voice): # remove main voice
            os.remove(main_voice)
        if os.path.exists("error.mp3"):
            os.remove("error.mp3")
