#show random 
import requests
import random
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

quotes = [quote.text for quote in soup.find_all('span', class_='text')]

random_quote = random.choice(quotes)

print("Random Quote:")
print(random_quote)