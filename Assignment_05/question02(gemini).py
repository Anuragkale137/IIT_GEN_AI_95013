import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

user_prompt = input("Enter your prompt: ")

req_data = {
    "model": "gemini-2.0-flash",
    "messages": [
        {
            "role": "user",
            "content": user_prompt
        }
    ]
}

response = requests.post(url, headers=headers, json=req_data)

print("Status:", response.status_code)

if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(response.json())
