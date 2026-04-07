import requests
import json
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

data = []

while url:
    responce = requests.get(url)

    if responce.status_code != 200:
        print(responce.status_code)
        break

    soup = BeautifulSoup(responce.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        quotes = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        data.append({"quote": quotes, "author": author})

    nextBtn = soup.find("li", class_="next")

    if nextBtn:
        nextPage = nextBtn.find("a")["href"]
        url = "https://quotes.toscrape.com" + nextPage
    else:
        url = None

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Quotes saved successfully!")
