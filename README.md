# Streambot
# WhatsBot - LLM Powered Chatbot

WhatsBot is a conversational chatbot powered by OpenAI's GPT-3.5-turbo, designed using Flask and Streamlit. This project allows users to interact with an AI-powered chatbot via a simple web interface.

## Features
- Real-time conversation using OpenAI GPT-3.5-turbo
- Streamlit interface for intuitive chat functionality
- Preserves chat history during the session for enhanced conversation flow
- Flask backend for flexible API interaction

## Prerequisites
Ensure you have the following installed:
- Python 3.10+
- `openai` library
- `streamlit`
- `Flask`
- `python-dotenv`

## Installation
1. **Clone the Repository**
```bash
git clone https://github.com/thilageeswariguruviah/whatsbot-chatbot.git
cd whatsbot-chatbot
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Set Up Environment Variables**
Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Application

### Step 1: Start the Flask Backend
Run the following command to start the backend API:
```bash
python app.py
```

### Step 2: Start the Streamlit Frontend
In a separate terminal, run:
```bash
streamlit run streamlit_app.py
```

## Usage
1. Open your browser and visit: [http://localhost:8501](http://localhost:8501)
2. Enter your query in the text input field and click **Send**.
3. The chatbot will respond with a generated reply while maintaining conversation context.

## Project Structure
```
.
├── app.py             # Flask API for chatbot backend
├── llm.py             # Logic to interact with OpenAI's GPT-3.5-turbo
├── streamlit_app.py   # Streamlit frontend for user interaction
├── .env               # Environment variables (add your API key here)
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## Requirements File (`requirements.txt`)
```
openai
streamlit
Flask
python-dotenv
```

## Known Issues
- If the chatbot fails to generate a response, verify that your OpenAI API key is correctly set in the `.env` file.
- Ensure both the backend (`app.py`) and frontend (`streamlit_app.py`) are running simultaneously.

## Contributing
Contributions are welcome! If you encounter issues or have suggestions for improvement, feel free to submit a pull request or open an issue.


