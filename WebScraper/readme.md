# # Quotes Scraper

A Python web scraper that collects quotes and authors from https://quotes.toscrape.com and saves them into a JSON file.

## Features

* Scrapes quotes and authors
* Automatically navigates through all pages
* Stores results in a structured JSON file
* Handles pagination using the "Next" button

## Technologies Used

* Python
* requests
* BeautifulSoup (bs4)
* JSON

## How It Works

1. Sends an HTTP request to the website
2. Parses the HTML using BeautifulSoup
3. Extracts quote text and author names
4. Follows the "Next" button to move through pages
5. Collects all quotes into a list
6. Saves the results into a JSON file

## Output Example

```json
[
  {
    "quote": "The world as we have created it is a process of our thinking.",
    "author": "Albert Einstein"
  },
  {
    "quote": "It does not do to dwell on dreams and forget to live.",
    "author": "J.K. Rowling"
  }
]
```

## Installation

Install dependencies:

```bash
pip install requests beautifulsoup4
```w

Run the scraper:

```bash
python main.py
```

## Learning Goals

This project was built while learning web scraping with Python, focusing on:

* sending HTTP requests
* parsing HTML
* extracting structured data
* handling pagination
* saving scraped data
