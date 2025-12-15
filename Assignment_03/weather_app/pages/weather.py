import streamlit as st
import requests
import os

st.title("Weather Information")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )
    return requests.get(url).json()

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    data = get_weather(city)

    if data.get("cod") == 200:
        st.write(f" Temperature: {data['main']['temp']} °C")
        st.write(f" Humidity: {data['main']['humidity']} %")
    else:
        st.error("City not found or API error")
