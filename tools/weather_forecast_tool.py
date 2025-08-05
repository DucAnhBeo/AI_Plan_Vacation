import requests

WEATHER_API_KEY = "62c32d4a03e84ba7a0c13935250508"

def get_weather_forecast(input_text: str) -> str:
    # Expect input in format: "location,date"
    try:
        location, date = input_text.split(",")
        url = f"https://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={location}&dt={date.strip()}"
        res = requests.get(url)
        data = res.json()
        forecast = data["forecast"]["forecastday"][0]["day"]
        condition = forecast["condition"]["text"]
        avg_temp = forecast["avgtemp_c"]
        return f"Weather in {location} on {date}: {condition}, Avg Temp: {avg_temp}°C"
    except Exception as e:
        return f"Error fetching weather: {e}"
