import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")
prices = soup.find_all("p", class_="price_color")

for price in prices:
    price = price.text
    print(price)