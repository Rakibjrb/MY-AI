import os
import pvporcupine
from pvrecorder import PvRecorder
from config.dotenv import env

current_path = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(current_path, "voice_model", "Hey-Maya_en_linux_v4_0_0.ppn")

def listen_wake_word():
    # wake word access key & model path
    porcupine = pvporcupine.create(
        access_key=env["PICOVOICE_ACCESS_KEY"],
        keyword_paths=[MODEL_PATH]
    )

    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length) # microphone setup for listening the wake word
    
    try:
        recorder.start()
        print(f"Say: 'wake word'...")

        while True:
            pcm = recorder.read()
            result = porcupine.process(pcm)

            if result >= 0:
                recorder.stop()
                print("Maya Activated!")
                return True

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        porcupine.delete()
        recorder.delete()
