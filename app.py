import os
import requests
import streamlit as st
from dotenv import load_dotenv
from chatbot import get_response  # Import logic from chatbot.py

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("💬 Chat with AI")

# Sidebar button for "Clear Chat"
if st.sidebar.button("🔄 Clear Chat"):
    st.session_state.messages = []
    st.rerun()  # Use rerun to refresh the page after clearing the chat

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages in chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    bot_reply = get_response(st.session_state.messages)  # Get response from chatbot
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

