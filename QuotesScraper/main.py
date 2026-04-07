import requests
import json
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

data = []
try:
    with open("Author-Cache.json", "r") as f:
        authorCache = json.load(f)
except:
    authorCache = {}


def authorDetails(authorUrl):
    res = requests.get(authorUrl)
    if res.status_code != 200:
        print("Error uccored on Author page", res.status_code)
    soup = BeautifulSoup(res.text, "html.parser")
    d = soup.find("div", class_="author-details")
    name = d.find("h3", class_="author-title").text
    date = d.find("span", class_="author-born-date").text
    location = d.find("span", class_="author-born-location").text
    return name, date, location


while url:
    responce = requests.get(url)

    if responce.status_code != 200:
        print("Error uccored on first page", responce.status_code)
        break

    soup = BeautifulSoup(responce.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        tags = []
        authorUrl = ""
        quotesText = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tagsElements = q.find_all("a", class_="tag")
        newUrl = q.find("a")["href"]
        authorUrl = "https://quotes.toscrape.com" + newUrl
        if author in authorCache:
            name = author
            authorData = authorCache[author]
            date = authorData.get("date")
            location = authorData.get("location")
        else:
            name, date, location = authorDetails(authorUrl)
            authorCache[name] = {"date": date, "location": location}
            with open("Author-Cache", "w", encoding="utf-8") as f:
                json.dump(authorCache, f, indent=4)

        tagsText = []
        for i in tagsElements:
            tagsText.append(i.text)
        tags.append(tagsText)
        data.append(
            {
                "quote": quotesText,
                "author": author,
                "tags": tags,
                "name": name,
                "Date Of Birth": date,
                "Location": location,
            }
        )

    nextBtn = soup.find("li", class_="next")

    if nextBtn:
        nextPage = nextBtn.find("a")["href"]
        url = "https://quotes.toscrape.com" + nextPage
    else:
        url = None

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Quotes saved successfully!")
