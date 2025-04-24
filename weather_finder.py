import streamlit as st
import requests


def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"""
        📍 Weather in {data['name']}, {data['sys']['country']}
        🌡️ Temperature: {data['main']['temp']}°C
        💧 Humidity: {data['main']['humidity']}%
        🌬️ Wind Speed: {data['wind']['speed']} m/s
        🌤️ Condition: {data['weather'][0]['description'].title()}
        """
    else:
        return "❌ Error: City not found or API issue"


# Streamlit UI
st.title("Real-Time Weather App")

api_key = "ec1b974a58d6eccee14cbf2295b2b72f"

city = st.text_input("Enter city name", "")
if city:
    weather_info = get_weather(city, api_key)
    st.write(weather_info)

import streamlit as st

st.title("🌤️ Weather Finder")
st.write("Enter a city to get the weather forecast.")

