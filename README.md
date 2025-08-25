🤖 LangGraph Chatbot using OpenRouter + OpenAI

A conversational AI chatbot built using LangGraph, LangChain, and OpenRouter's OpenAI-compatible API.
This chatbot remembers conversations across sessions, supports multi-turn dialogue, and uses GPT-3.5-turbo for responses.

🚀 Features

🧠 LangGraph Workflow → Uses StateGraph to manage chatbot states.

🗨️ Multi-turn Conversation → Remembers previous messages.

🔄 Memory Support → Integrated with MemorySaver checkpointing.

🌐 OpenRouter API → Uses OpenRouter for OpenAI models.

⚡ Fast & Lightweight → Minimal setup, highly optimized.

🛠️ Easy Configuration → .env based API key management.

📂 Project Structure
chatbot-project/
│── chatbot.py          # Main chatbot implementation
│── .env                # Environment variables
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/langgraph-chatbot.git
cd langgraph-chatbot

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate      # For Linux / Mac
venv\Scripts\activate         # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the root directory:

OPENROUTER_API_KEY=your_openrouter_api_key_here

▶️ How to Run
python chatbot.py


Example:

type here: Hello
AI: Hi there! How can I help you today?

type here: What is the capital of India?
AI: The capital of India is New Delhi.

type here: quit
