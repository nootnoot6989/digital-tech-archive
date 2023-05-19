import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL to scrape
URL = "https://www.pokemoncenter.com/category/trading-card-game"

# Send a GET request to the URL
data = requests.get(URL)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(data.content, 'html.parser')

# Find all products on the page
products = soup.find_all('div', class_='feNDW0JlPtJ60lRMSpEuYw')

# Loop through each product and extract its name, price and href link
product_data = []
for product in products:
    name = product.find('h3', class_='lz7HXA36ucyAMjcM15HZvQ').text.strip()
    price_element = product.find('span', class_='uqHtS95QbSSfoQRs-uyNWw').text.strip() #.replace('\n', '').replace('\t', '').replace('+', '')
    product_href = product.find('a').get('href')

    # Have to store all scraped data into one variable because '.append' only takes in one arguement
    data = name, price_element, product_href
    product_data.append(data)

print(data)

# Exprots product_data into a viewable .csv file
df = pd.DataFrame(product_data, columns=['Product Name', 'Price', 'Href'])
df.to_csv('guf_product_data.csv', index=False)