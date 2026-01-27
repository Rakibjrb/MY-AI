# MY-AI

## File Structure

```
|-- src
|   |-- brain                      # AI Brain folder
|   |   |-- ai_model.py            # AI Model file
|   |   |-- short_memory.py        # AI short term memory & gemini response handler
|   |
|   |-- config                     # AI Configuration
|   |   |-- dotenv.py              # AI environment variables load in a object
|   |   
|   |-- handlers                   # AI Handlers for different tasks
|   |   |-- local_commands.py      # AI Local Commands Handler
|   |   |-- system_commands.py     # AI System Commands Handler
|   |   |-- commands.py            # AI Commands Handler
|   |  
|   |-- local_functions            # Local Functions for AI
|   |   |-- saytime.py             # AI Say Time Function
|   |   |-- startup.py             # AI Startup Function
|   |   
|   |-- speak_and_listen           # AI Speak and Listen functionalities
|   |   |-- voice_model            # AI voice model for wake word
|   |   |   |-- voice_model_file   # wake word model file from picovoiceai console
|   |   |
|   |   |-- speak.py               # AI Speak functionalities
|   |   |-- listen.py              # AI Listen functionalities
|   |   |-- wake.py                # AI Wake word functionalities
|   |   |-- main.py                # Main Program File for running the AI
|
|-- README.md                      # README File
|-- requirements.txt               # Requirements File

```