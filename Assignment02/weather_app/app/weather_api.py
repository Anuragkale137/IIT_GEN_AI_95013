import requests
from config import api_key, base_url, units

def get_weather_data(city):
    url = f"{base_url}?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        return None