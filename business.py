import os
import requests
from dotenv import load_dotenv

def call_api(call, path):
    try:
        response = requests.request(call, path, timeout=10)
        return response.json()
    except requests.exceptions as e:
        return f"API Call Error {e}"


def get_path(city):
    return f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=Metric&appid={os.getenv("API_KEY")}"


def get_weather(city):
    """
    Get the weather forecast of a given city.
    """
    data = call_api("GET", get_path(city))
    weather = data["list"]
    temp = []

    if data:
        for i, t in enumerate(weather):
            temp.append(t["main"]["temp"])
            formatted_data = {
                "date": t["dt_txt"],
                "temp": temp
            }
    else:
        return "No data available"
    return formatted_data

load_dotenv()