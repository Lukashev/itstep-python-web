import requests
from bs4 import BeautifulSoup
import json

def start():
    urls = [
        'https://www.books.ru/biznes-9000032/?page=1',
        'https://www.books.ru/biznes-9000032/?page=2',
        'https://www.books.ru/biznes-9000032/?page=3',
        'https://www.books.ru/biznes-9000032/?page=4',
        'https://www.books.ru/biznes-9000032/?page=5'
    ]

    result = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        books = soup.find_all('div', class_="book-catalog_item")
        for book in books:
            image = book.find('img')['src']
            title = book.find('a', class_='book-catalog_item_title').string.strip()
            price = book.find('span', class_='book-price')
            currency = price.span.extract()
            formatted_price = price.string.strip()
            formatted_currency = currency.string.strip()
            result.append({'title': title, 'price': f"{formatted_price} {formatted_currency}", 'image': image})

    data = {'count': len(result), 'books': result}

    with open('./part6/static/books.json', 'w', encoding='utf-8') as file:
        json_string = json.dumps(data, ensure_ascii=False).encode('utf-8')
        file.write(json_string.decode())


if __name__ == '__main__':
    start()