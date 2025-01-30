import requests
import pandas as pd

API_KEY = 'YOUR_API_KEY'
LOCATION = '33.5268529,47.6093922'
RADIUS = 5000  # Radius in meters

url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LOCATION}&radius={RADIUS}&key={API_KEY}'
response = requests.get(url)
data = response.json()

businesses = []
for place in data['results']:
    businesses.append({
        'Name': place.get('name'),
        'Address': place.get('vicinity'),
        'Phone': place.get('formatted_phone_number', 'N/A'),  # Phone number may not be available
        'Type': place.get('types', [])
    })

df = pd.DataFrame(businesses)
df.to_excel('businesses.xlsx', index=False)




