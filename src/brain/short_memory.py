from brain.ai_model import model

def get_gemini_response(user_input):
    try:
        response = model.send_message(user_input)
        return response.text
    except Exception as e:
        print(f"Error : {e}")
        return "Error : Something went wrong. Look at terminal for more details."