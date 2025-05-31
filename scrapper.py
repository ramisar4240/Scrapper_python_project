
from bs4 import BeautifulSoup
import requests
import json

url = "https://books.toscrape.com/"

def scrape_book(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the URL")
        return

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    book_data = []

    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]

        book_data.append({
            "title": title,
            "currency": currency,
            "price": price
        })

    # Save the JSON data to a file
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(book_data, f, ensure_ascii=False, indent=4)

    print("Book data has been saved to 'books.json'.")

scrape_book(url)
