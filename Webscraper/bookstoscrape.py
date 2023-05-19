import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL to scrape
URL = "https://books.toscrape.com/catalogue/page-1.html"

# Send a GET request to the URL
response = requests.get(URL)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all products on the page
products = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

# Loop through each product and extract its name, price and href link
product_data = []
for product in products:
    name = product.find('h3').text.strip()
    price_element = product.find('p', class_='price_color').text.strip()
    product_href = product.find('a').get('href')

    # Have to store all scraped data into one variable because '.append' only takes in one arguement
    data = name, price_element, product_href
    product_data.append(data)

print(data)

# Exprots product_data into a viewable .csv file
df = pd.DataFrame(product_data, columns=['Product Name', 'Price', 'Href'])
df.to_csv('books_product_data.csv', index=False)