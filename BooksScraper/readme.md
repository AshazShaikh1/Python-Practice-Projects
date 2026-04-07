# Books Dataset Scraper

A Python web scraper that collects book information from https://books.toscrape.com and stores it in a structured JSON dataset.

## Features

* Scrapes book titles
* Extracts book price
* Extracts book rating
* Automatically navigates through all pages
* Saves collected data to a JSON file

## Data Collected

For each book the scraper collects:

* Book title
* Price
* Rating

Example output:

```json
{
  "name": "A Light in the Attic",
  "price": "£51.77",
  "rating": "Three"
}
```

## Technologies Used

* Python
* requests
* BeautifulSoup
* JSON

## How It Works

1. Sends an HTTP request to the website
2. Parses the HTML using BeautifulSoup
3. Finds book containers (`article.product_pod`)
4. Extracts book title, rating, and price
5. Detects the next page using pagination
6. Continues scraping until the last page
7. Saves the final dataset to `books.json`

## Installation

Install dependencies:

```bash
pip install requests beautifulsoup4
```

Run the scraper:

```bash
python main.py
```

## Learning Goals

This project was built while learning web scraping concepts such as:

* HTML parsing
* pagination scraping
* extracting nested elements
* handling relative URLs
* creating structured datasets
