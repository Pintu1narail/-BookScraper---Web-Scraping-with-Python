import requests
from bs4 import BeautifulSoup
import csv

base_url = 'http://books.toscrape.com/catalogue/'
current_page = 'page-1.html'

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
}

with open('book_Scrape.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Stock_status", "Rating"])
    
    while current_page:
        response = requests.get(base_url + current_page, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        print(f"Scrape Running....{base_url + current_page}")
    
        for book in books:
            title = book.h3.a['title']
            rating = book.find('p', class_='star-rating')['class'][1]
            price = book.find('p', class_='price_color').get_text(strip=True)[2:]
            stock = book.find('p', class_='instock availability').get_text(strip=True)
            
            rating_number = rating_map.get(rating, 0)
            writer.writerow([title, price, stock, rating_number])
        
            next_page = soup.find('li', class_='next')
            if next_page:
                current_page = next_page.find('a')['href']
            else:
                current_page = None
        
print("Books Scraping Completed!") 