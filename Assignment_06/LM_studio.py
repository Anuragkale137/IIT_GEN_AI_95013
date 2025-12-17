#loacl lm studio based chatbot using groq api#cloud based chatbot using groq api
import requests
import json
import os
import time
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

def LM_studio_chatbot(user_prompt):

    api_key = "dummy_key"
    url = "http://127.0.0.1:1234/v1/chat/completions"
    header = {
        "content-type":"application/json",
        "Authorization":f"Bearer {api_key}"
    }

    #user_prompt = st.chat_input("chat with me:")
    if user_prompt:
        req_data = {
            "model": "phi-3-mini-4k-instruct",
            "messages":[
                {"role":"user","content":user_prompt}
            ]
        }
        response = requests.post(url,headers = header, data = json.dumps(req_data))
        resp = response.json()
        return (resp["choices"][0]["message"]["content"])
