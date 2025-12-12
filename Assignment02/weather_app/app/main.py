from weather_api import get_weather_data

def display_weather():
    city = input("Enter city name:")
    data = get_weather_data(city)
    if data:
        print("temperature:",data["main"]["temp"])
        print("humdity:",data["main"]["humidity"])
    else:
        print("failed to retrive data")

if __name__ == "__main__":
    display_weather()