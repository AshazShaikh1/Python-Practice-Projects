import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

url = "https://books.toscrape.com/index.html"
booksData = []
try:
    with open("books.json", "r") as f:
        booksData = json.load(f)
except:
    booksData = []

while url:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error loading {url} with {response.status_code}")
        break
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for b in books:
        rating = b.find("p", class_="star-rating")["class"][1]
        bookname = b.find("h3").find("a")["title"]
        price = (
            b.find("div", class_="product_price").find("p", class_="price_color").text
        )
        booksData.append({"name": bookname, "price": price, "rating": rating})

    nextBtn = soup.find("li", class_="next")
    if nextBtn:
        nextPage = nextBtn.find("a")["href"]
        url = urljoin(url, nextPage)
        print(url)
    else:
        url = None

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(booksData, f, indent=4)

print("Succfully created books.json")
