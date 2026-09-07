import os
import requests
from dotenv import load_dotenv

load_dotenv()

@tool
def get_weather(city: str):
    """
      Get current weather information for a city.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    data = response.json()

    if response.status_code != 200:
        return {
            "error": data.get("message", "Unable to get weather")
        }

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }

    return weather_data
