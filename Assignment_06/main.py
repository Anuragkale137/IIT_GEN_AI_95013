import streamlit as st
import time
import os
import requests
import json
import LM_studio
import groq
from dotenv import load_dotenv
load_dotenv()
from LM_studio import LM_studio_chatbot
from groq import groq_chatbot

st.title("Chatbot App")
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("Menu")
    st.header("Select Chatbot Type")
    chatbot_type = st.selectbox("Choose a chatbot:", ("Local LM Studio Chatbot", "GROQ Cloud Chatbot"))

if chatbot_type == "Local LM Studio Chatbot":
    user_prompt = st.chat_input("Ask me anything (Local LM Studio):")
    if user_prompt:
        data = LM_studio_chatbot(user_prompt)
        st.session_state.messages.append(data)
        for msg in st.session_state.messages:
                st.write(msg)
            # print(msg)

else:
    user_prompt = st.chat_input("Ask me anything (GROQ Cloud):")
    if user_prompt:
        data1 = groq_chatbot(user_prompt)
        st.session_state.messages.append(data1)
        for msg in st.session_state.messages:
                st.write(msg)