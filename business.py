import os
import requests
from dotenv import load_dotenv
from datetime import datetime

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
            temp.append({
                "date": t["dt_txt"],
                "temp": t["main"]["temp"],
                "temp_min": t["main"]["temp_min"],
                "temp_max": t["main"]["temp_max"]
            })
        formatted_data = {
            "weather": temp
        }
    else:
        return "No data available"
    return formatted_data

load_dotenv()