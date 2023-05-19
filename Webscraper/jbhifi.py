import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL to scrape
URL = "https://www.jbhifi.com.au/collections/collectibles-merchandise/pokemon-trading-cards"

# Send a GET request to the URL
data = requests.get(URL)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(data.content, 'html.parser')

# Find all products on the page
products = soup.find_all('a', class_='_1gvvwld0 _1gvvwld1 _1gvvwld2')

# Loop through each product and extract its name, price and href link
product_data = []
for product in products:
    name = product.find('div', class_='_1gvvwldd _1gvvwlde').text.strip()
    price_element = product.find('span', class_='PriceFont_fontStyle__w0cm2q1 PriceTag_actual_small__1eb7mu9o PriceTag_actualDefault__1eb7mu9m').text.strip() #.replace('\n', '').replace('\t', '').replace('+', '')
    product_href = product.find('a').get('href')

    # Have to store all scraped data into one variable because '.append' only takes in one arguement
    data = name, price_element, product_href
    product_data.append(data)

print(data)

# Exprots product_data into a viewable .csv file
df = pd.DataFrame(product_data, columns=['Product Name', 'Price', 'Href'])
df.to_csv('jbhifi_product_data.csv', index=False)