from bs4 import BeautifulSoup
from requests import get, Response
import pandas as pd
import itertools
import matplotlib.pyplot as plt
# library for statistical high visualization of data
import seaborn as sns
import re

sns.set()

"""
Header to pass along the get command just to make the queries look like
they are actually coming from an actual browser.
"""
headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebkit/537.36 (KHTML, '
                'like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

url = "https://casa.sapo.pt/Venda/Apartmentos/?sa=11&or=10"
response = get(url, headers=headers)  # type: Response


# parsing the info to make it easier to navigate and get the contents
html_soup = BeautifulSoup(response.text, 'html.parser')  # type: BeautifulSoup

house_containers = html_soup.find_all('div', class_='searchResultProperty')
first_structure = house_containers[0]
price = first_structure.find_all('span')[2].text
price = price.encode('utf-8').replace(' ', '')

# get only digits
price = re.sub('\D', '', price)
# using itertools to retrieve and turn the price into int
price = int(''.join(itertools.takewhile(str.isdigit, price)))


for url in first_structure.find_all('a'):
    print(url.get('href'))