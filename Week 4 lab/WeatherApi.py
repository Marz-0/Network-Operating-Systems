import socket
import requests
import json
from datetime import datetime

# Constants for London coordinates and API URL
LONDON_LAT = 51.5074
LONDON_LON = -0.1278
API_URL = (f"https://api.open-meteo.com/v1/forecast?"
           f"latitude={LONDON_LAT}&longitude={LONDON_LON}"
           f"&hourly=temperature_2m,precipitation_probability,windspeed_10m"
           f"&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset"
           f"&current_weather=true&timezone=Europe/London")

def fetch_weather_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def extract_current_weather(weather_data):
    current = weather_data["current_weather"]
    return current["temperature"], current["windspeed"]

def extract_daily_forecast(weather_data, date):
    daily = weather_data["daily"]
    if date in daily["time"]:
        index = daily["time"].index(date)
    else:
        index = 0
    return (daily["temperature_2m_max"][index],
            daily["temperature_2m_min"][index],
            daily["sunrise"][index],
            daily["sunset"][index])

def format_weather_report(current_temp, current_wind, max_temp, min_temp, sunrise, sunset):
    return (f"London Weather Report\n"
            f"---------------------\n"
            f"Current temperature: {current_temp}°C\n"
            f"Current wind speed: {current_wind} km/h\n"
            f"Today's high: {max_temp}°C\n"
            f"Today's low: {min_temp}°C\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}\n")

def main():
    weather_data = fetch_weather_data(API_URL)
    current_temp, current_wind = extract_current_weather(weather_data)
    today = datetime.now().strftime("%Y-%m-%d")
    max_temp, min_temp, sunrise, sunset = extract_daily_forecast(weather_data, today)
    report = format_weather_report(current_temp, current_wind, max_temp, min_temp, sunrise, sunset)
    print(report)

if __name__ == "__main__":
    main()