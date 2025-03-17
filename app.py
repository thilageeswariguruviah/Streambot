# app.py
import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, Response

app = Flask(__name__)


load_dotenv()  # Load environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_input):
    """
    Sends the user_input to the LLM (using OpenAI API) and returns the generated response.
    Adjust parameters as needed.
    """
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Change if you prefer a different engine/model
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None,
        )
        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        print("Error generating response:", e)
        return "Sorry, I encountered an error processing your request."
    
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)

