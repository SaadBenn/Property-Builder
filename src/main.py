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

STOP = 9
n_pages = 0

# Setting up the lists that will form our dataframe with all the results
titles = []
created = []
prices = []
areas = []
zone = []
condition = []
descriptions = []
urls = []
thumbnails = []

for page in range(0, STOP):
    n_pages += 1
    url = 'https://casa.sapo.pt/Venda/Apartmentos/?sa=11&lp=10000&or=10' + '&pn='+str(page)
    response = get(url, headers=headers)  # type: Response

    # parsing the info to make it easier to navigate and get the contents
    html_soup = BeautifulSoup(response.text, 'html.parser')  # type: BeautifulSoup

    house_containers = html_soup.find_all('div', class_='searchResultProperty')

    # making sure house container is not null -- defensive programming
    if house_containers:
        for container in house_containers:

            # element 2 is the price
            price = container.find_all('span')[2].text
            if price == 'Contacte Anunciante':
                # next element is the price
                price = container.find_all('span')[3].text
                if price.find('/') != -1:
                    price = price[0:price.find['/']-1]
            if price.find('/') != -1:
                price = price[0:price.find('/')-1]

            # using list comprehension to simplify the code a bit
            # get the price as int
            price_ = [int(price[s]) for s in range(0, len(price)) if price[s].isdigit()]

            # stringify the price
            price = ''
            for digit in price_:
                price = price + str(digit)

            # build the price database
            prices.append(int(price))

            # Populating zones list
            location = container.find_all('p', class_='searchPropertyLocation')[0].text
            location = location[7:location.find(',')]
            zone.append(location)

            # populating titles list
            name = container.find_all('span')[0].text
            titles.append(name)

            # populating status list
            status = container.find_all('p')[5].text
            condition.append(status)

            # populate area list
            m2 = container.find_all('p')[9].text
            m2 = m2.encode('utf-8').replace(' ', '')
            if m2 != '-':
                m2 = re.sub('\D', '', m2)
                m2 = float(''.join(itertools.takewhile(str.isdigit, m2)))
                areas.append(m2)
            else:
                areas.append(m2)

print(areas)
# first_structure = house_containers[0]
# price = first_structure.find_all('span')[2].text
# price = price.encode('utf-8').replace(' ', '')

# # get only digits
# price = re.sub('\D', '', price)
# # using itertools to retrieve and turn the price into int
# price = int(''.join(itertools.takewhile(str.isdigit, price)))



#
# for url in first_structure.find_all('a'):
#     print(url.get('hr ef'))