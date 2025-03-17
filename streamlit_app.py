# streamlit_app.py
import streamlit as st
from llm import generate_response

st.title("WhatsBot - LLM Powered Chatbot")
st.write("Chat with the WhatsBot. This interface is for demo purposes.")

# Initialize conversation history in session state if not already set
if "history" not in st.session_state:
    st.session_state.history = []

# Capture user input; the text input is not stored in session_state directly to avoid widget state conflicts.
user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        # Generate a response while preserving conversation context
        bot_reply, updated_history = generate_response(user_input, st.session_state.history)
        st.session_state.history = updated_history

# Display the conversation history in a chat-like format
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**Bot:** {msg['content']}")
