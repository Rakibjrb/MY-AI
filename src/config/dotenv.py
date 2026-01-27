from dotenv import load_dotenv
import os

load_dotenv()

env = {
    "PICOVOICE_ACCESS_KEY": os.getenv("PICOVOICE_ACCESS_KEY"),
    "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
    "GEMINI_AI_MODEL": os.getenv("GEMINI_AI_MODEL")
}