import os
import requests

from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """
    Get the current real-time weather information for a city.

    Use this tool when the user asks about weather,
    temperature, humidity, wind, or current weather conditions.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "Error: OPENWEATHER_API_KEY is missing."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return f"""
            City: {weather["city"]}
            Temperature: {weather["temperature"]}°C
            Feels Like: {weather["feels_like"]}°C
            Humidity: {weather["humidity"]}%
            Weather: {weather["description"]}
            Wind Speed: {weather["wind_speed"]} m/s
        """

    except requests.exceptions.RequestException as e:
        return f"Unable to get weather information: {str(e)}"