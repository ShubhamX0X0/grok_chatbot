import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load the .env file to get your API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Function to talk to Groq
def get_response(user_input):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, something went wrong!"

# Streamlit UI
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("💬 Chat with Groq AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    bot_reply = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)


