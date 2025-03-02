import requests
from datetime import datetime, timedelta

# Enter your API key
api_key = 'API_KEy'

# Function to get the city's geographic coordinates
def get_coordinates(city_name, country_code):
    try:
        geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={api_key}'
        print(f"Requesting coordinates from URL: {geocoding_url}")
        response = requests.get(geocoding_url)
        print(f"Response status code: {response.status_code}")
        response.raise_for_status()  # Check for errors
        data = response.json()
        if data:
            print(f"Coordinates found: {data[0]['lat']}, {data[0]['lon']}")
            return data[0]['lat'], data[0]['lon']
        else:
            print("No data found for the specified city.")
            return None, None
    except requests.HTTPError as http_err:
        if response.status_code == 401:
            print("Unauthorized access - please check your API key.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None, None
    except Exception as err:
        print(f"Error fetching geographic coordinates: {err}")
        return None, None

def get_weather_data(lat, lon, timestamp):
    try:
        url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}&units=metric&lang=en'
        print(f"Requesting weather data from URL: {url}")
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        response.raise_for_status()  # Check for errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    city_name = input("Enter city name: ")
    country_code = input("Enter country code (e.g., 'IR' for Iran): ")
    days_ago = int(input("How many days ago? "))
    date = datetime.now() - timedelta(days=days_ago)
    timestamp = int(datetime.timestamp(date))

    lat, lon = get_coordinates(city_name, country_code)

    if lat and lon:
        data = get_weather_data(lat, lon, timestamp)
        if data and 'current' in data:
            print(f"Weather report for '{city_name}' on {date.strftime('%Y-%m-%d')}:")
            print(f"Temperature: {data['current']['temp']}°C")
            print(f"Weather: {data['current']['weather'][0]['description']}")
            print(f"Humidity: {data['current']['humidity']}%")
            print(f"Wind Speed: {data['current']['wind_speed']} m/s")
            print(f"Pressure: {data['current']['pressure']} hPa")
        else:
            print("No data available for the specified date.")
    else:
        print("City coordinates not found.")

if __name__ == "__main__":
    main()
