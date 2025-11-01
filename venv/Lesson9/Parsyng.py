import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("h3")

for book in books:
    title = book.a["title"]
    print(title)