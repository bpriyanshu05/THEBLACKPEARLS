import requests
from bs4 import BeautifulSoup
import csv
import time

def get_quotes_from_page(url):
    quotes = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    # Find the div with id 'all_quotes'
    table = soup.find('div', attrs={'id': 'all_quotes'})

    if table:
        for row in table.findAll('div', attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
            quote = {}
            try:
                quote['theme'] = row.h5.text
                quote['url'] = row.a['href']
                quote['img'] = row.img['src']
                alt_text = row.img['alt']
                if " #" in alt_text:
                    quote['lines'], quote['author'] = alt_text.split(" #")
                else:
                    quote['lines'] = alt_text
                    quote['author'] = 'Unknown'
                quotes.append(quote)
            except AttributeError as e:
                print(f"Error processing row: {e}")
    return quotes

def get_all_quotes(base_url):
    all_quotes = []
    page_number = 1

    while True:
        url = f"{base_url}?page={page_number}"
        print(f"Scraping page: {page_number}")
        quotes = get_quotes_from_page(url)
        if not quotes:
            break
        all_quotes.extend(quotes)
        page_number += 1
        time.sleep(1)  # Be polite and don't hammer the server

    return all_quotes

def save_quotes_to_csv(quotes, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['theme', 'url', 'img', 'lines', 'author'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)

if __name__ == "__main__":
    BASE_URL = "http://www.values.com/inspirational-quotes"
    all_quotes = get_all_quotes(BASE_URL)
    save_quotes_to_csv(all_quotes, 'inspirational_quotes.csv')
    print(f"Scraped {len(all_quotes)} quotes.")
