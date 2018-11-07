from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

"""
Header to pass along the get command just to make the queries look like
they are actually coming from an actual browser.
"""
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebkit/537.36 (KHTML, '
            'like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

url = "https://casa.sapo.pt/Venda/Apartmentos/?sa=11&or=10"
response = get(url, headers=headers)

print(response)
print(response.text[:1000])