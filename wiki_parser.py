# import libraries
import requests
from bs4 import BeautifulSoup
import re

# specify the url
website = 'https://en.wikipedia.org/wiki/List_of_Intel_codenames'

# query the website and return the html to the variable ‘page’
page = requests.get(website)
content = page.content

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(content, 'html.parser')

names = [div.find('td') for div in soup.findAll('tr')]

for name in names:
  _name = str(name).replace('<td>', '')
  formatted_name = str(_name).replace('</td>', '')
  if '<' not in formatted_name:
    print(formatted_name, end=",\n")
