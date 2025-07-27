import requests

API_KEY = "75c4d24043931627e4b60beadf4bfab3"  # Replace with your API Key:)))
CITY = "Tehran"  # Your target city
UNITS = "metric"  # Celsius (use "imperial" for Fahrenheit)...
FORECAST_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"

response = requests.get(FORECAST_URL)
data = response.json()

if response.status_code == 200:
    for forecast in data["list"][:5]:  # First 5 forecasts
        date = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        weather = forecast["weather"][0]["description"]
        print(f"{date} → Temp: {temp}°C, Weather: {weather}")
else:
    print("Forecast error:", data.get("message"))