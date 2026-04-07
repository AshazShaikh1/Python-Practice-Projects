# Quotes Scraper with Author Details

A Python web scraper that collects quotes, tags, and detailed author information from https://quotes.toscrape.com.

The scraper automatically navigates through all pages, visits author pages for additional details, and stores the collected data in a structured JSON format.

## Features

* Scrapes quotes from multiple pages
* Extracts quote text and author
* Collects tags associated with each quote
* Visits author pages to gather additional information
* Stores author data in a cache to avoid repeated requests
* Saves the final dataset as JSON

## Data Collected

For each quote the scraper collects:

* Quote text
* Author name
* Tags
* Author birth date
* Author birth location

Example output:

```json
{
  "quote": "The world as we have created it is a process of our thinking.",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "thinking"],
  "name": "Albert Einstein",
  "Date Of Birth": "March 14, 1879",
  "Location": "Ulm, Germany"
}
```

## Technologies Used

* Python
* requests
* BeautifulSoup (bs4)
* JSON

## How It Works

1. Sends HTTP requests to the quotes website
2. Parses HTML pages using BeautifulSoup
3. Extracts quote text, author, and tags
4. Follows the author page link to collect additional author details
5. Uses a caching system to avoid requesting the same author page multiple times
6. Stores all collected data in a JSON file

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

* Pagination scraping
* Nested HTML parsing
* Multi-page data extraction
* Request optimization using caching
* Structuring scraped data
