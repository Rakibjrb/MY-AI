import asyncio
import edge_tts as tts
import os
import subprocess
import langdetect

#Female voice
ENG_VOICE = "en-US-AvaNeural"
BN_VOICE = "bn-BD-NabanitaNeural"

#Male voice
# ENG_VOICE = "en-US-AndrewNeural" 
# BN_VOICE = "bn-BD-PradeepNeural"

detected_lang = 'en'

async def generate_voice(text):
    voice_file_name = "voice.mp3"
    try:
        try:
            detected_lang = langdetect.detect(text)
        except:
            detected_lang = "en"
        
        voice = tts.Communicate(text, detected_lang == "en" and ENG_VOICE or BN_VOICE)
        await voice.save(voice_file_name)
        print(f"Maya Speaking {detected_lang}...")
        os.system("pactl set-sink-volume @DEFAULT_SINK@ 80%")
        subprocess.run(["mpg123", "-q", voice_file_name])

    except Exception as e:
        print(f"Voice Error: {e}")
    
    finally:
        if os.path.exists(voice_file_name):
            os.remove(voice_file_name)

def speak(text):
    asyncio.run(generate_voice(text))