# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:21:04 2024

@author: Shriharan S
"""
import requests
from bs4 import BeautifulSoup
import csv

def scrape_books(url, csv_file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.select('article.product_pod')
        
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Price', 'Rating'])
            
            for book in books:
                title = book.h3.a['title']
                price = book.select_one('.price_color').get_text(strip=True)
                rating = book.p['class'][1]  # The second class of the <p> tag represents the rating
                
                writer.writerow([title, price, rating])
        
        print(f"Data has been successfully scraped and saved to {csv_file_path}")
    
    except requests.RequestException as e:
        print(f"Error connecting to the website: {e}")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

if __name__ == "__main__":
    url = "http://books.toscrape.com/"
    csv_file_path = "books_data.csv"
    scrape_books(url, csv_file_path)
