#cloud based chatbot using groq api
import requests
import json
import os
import time
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

def groq_chatbot(user_prompt):
        

    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    header = {
        "content-type":"application/json",
        "Authorization":f"Bearer {api_key}"
    }


    #user_prompt =st.chat_input("User:")
    if user_prompt:
        req_data = {
            "model": "llama-3.3-70b-versatile",
            "messages":[
                {"role":"user","content":user_prompt}
            ]
        }
        response = requests.post(url,headers = header, data = json.dumps(req_data))
        resp = response.json()
        return (resp["choices"][0]["message"]["content"])