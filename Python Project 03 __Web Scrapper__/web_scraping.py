# -*- coding: utf-8 -*-
"""Web Scraping Tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-yE7ZJA9KJE0xhOfxXh_FouzwsFp7gAC

##Making web scrapper
"""

#!pip install requests bs4

import pandas as pd
import requests
from bs4 import BeautifulSoup

"""**Installing and importing necessary libraries**"""

WEBSITE = "https://books.toscrape.com"
html_content = requests.get(WEBSITE).content

"""*Selecting website to scrape*"""

soup = BeautifulSoup(html_content)
side_categories = soup.find("ol", class_="row")

list_items = side_categories.find_all("h3")

"""*Selecting data to scrape from the HTML file of the website*"""

cat_names = []
cat_links = []
cat_price = []
cat_stock = []
for item in list_items:
    cat_names.append(item.text.strip())
    # cat_links.append(item['href'])
    # cat_price.append(item['p'])

"""**Defining variables**"""

soup = BeautifulSoup(html_content)
side_categories = soup.find("ol", class_="row")

list_price = side_categories.find_all("p", class_ = "price_color")

"""Selecting data to scrape from the HTML file of the website *2"""

soup = BeautifulSoup(html_content)
side_categories = soup.find("ol", class_="row")

list_stock = side_categories.find_all("p", class_ = "instock availability")

"""
Selecting data to scrape from the HTML file of the website *3"""

for price in list_price:
    cat_price.append(price.text.strip())
    # cat_stock.append(stock.text.strip())

for stock in list_stock:
    cat_stock.append(stock.text.strip())

"""***Creating dataframe to use pandas for making the csv file***"""

df = pd.DataFrame({
    'category_name': cat_names,
    'category_price': cat_price,
    'category_stock': cat_stock
    # 'category_links': cat_links
})

df.head(n=10)

"""**Saving the csv file**"""

df.to_csv("category_data.csv")