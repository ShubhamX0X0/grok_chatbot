import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def get_response(messages):
    """
    Function to interact with Groq API and return a response.
    :param messages: List of messages to pass to the model.
    :return: Response from Groq API or an error message.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}] + messages
    }

    try:
        # Send the request to Groq API
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=15
        )
        response.raise_for_status()  # Raise an error if the status code is not 200
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error:", e)
        return "Sorry, something went wrong."
