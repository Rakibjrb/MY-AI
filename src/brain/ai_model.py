from google import genai
from google.genai import types
from config.dotenv import env

# client = genai.Client(api_key=env["GEMINI_API_KEY"]) # Configure the Gemini API key
client = genai.Client(api_key=env["GEMINI_API_KEY"])
use_ai_model = env["GEMINI_AI_MODEL"]

# see list of ai models available for your api key
# print("--- Available Models ---")
# for model in client.models.list():
#     print(model.name)
# print("------------------------")

# set instruction for gemini to act like maya
instructions = [
    "You are Maya, a smart and friendly female AI assistant.",
    "You are talking to Rakibul Hasan.",
    "Keep answers short and natural.",
    "Always act like a helpful companion, not just a robot.",
    "If Rakibul speaks in Bengali, reply in Bengali. If in English, reply in English.",
]

# # select model
chat_session = client.chats.create(
    model=use_ai_model,
    config=types.GenerateContentConfig(
        system_instruction=instructions,
        temperature=0.7,
    )
)

model = chat_session