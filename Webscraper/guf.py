import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL to scrape
URL = "https://guf.com.au/search?type=product&options%5Bprefix%5D=last&q=pokemon+tcg"

# Send a GET request to the URL
data = requests.get(URL)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(data.content, 'html.parser')

# Find all products on the page
products = soup.find_all('div', class_='grid-view-item__link grid-view-item__image-container')

# Loop through each product and extract its name, price and href link
product_data = []
for product in products:
    name = product.find('div', class_='h4 grid-view-item__title').text.strip()
    price_element = product.find('span', class_='product-price__price is-bold qv-regularprice').text.strip() #.replace('\n', '').replace('\t', '').replace('+', '')
    product_href = product.find('a').get('href')
    link = ("https://guf.com.au" + product_href)

    # Have to store all scraped data into one variable because '.append' only takes in one arguement
    data = name, price_element, link
    product_data.append(data)

print(data)

# Exprots product_data into a viewable .csv file
df = pd.DataFrame(product_data, columns=['Product Name', 'Price', 'Href'])
df.to_csv('guf_product_data.csv', index=False)