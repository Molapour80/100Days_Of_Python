import requests

API_KEY = "75c4d24043931627e4b60beadf4bfab3"  # Replace with your API Key:)))
CITY = "Tehran"  # Your target city
UNITS = "metric"  # Celsius (use "imperial" for Fahrenheit)...

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    print(f"Weather in {CITY}:")
    print(f"Conditions: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error fetching data:", data.get("message", "Unknown error"))


