# llm.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")
# Set the model name to a chat model. Use "gpt-4" if you have access, otherwise "gpt-3.5-turbo"
MODEL_NAME = "gpt-3.5-turbo"

def generate_response(user_input, conversation_history=None):
    """
    Uses the OpenAI ChatCompletion API to generate a response.
    conversation_history should be a list of messages in the format:
      {"role": "user" or "assistant", "content": "message content"}
    """
    if conversation_history is None:
        conversation_history = []

    # Append the new user message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.7,
            max_tokens=150,
        )
        # Extract the assistant's reply
        reply = response.choices[0].message["content"].strip()
        # Append the assistant's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": reply})
        return reply, conversation_history
    except Exception as e:
        print("Error generating response:", e)
        return "Sorry, I encountered an error processing your request.", conversation_history
