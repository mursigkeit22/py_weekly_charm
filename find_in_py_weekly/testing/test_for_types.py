import re

from bs4 import BeautifulSoup
import bs4
from typing import List
import requests
from bs4 import BeautifulSoup

page_link = 'https://pycoders.com/issues/' + str(411)
page_response = requests.get(page_link)  # <class 'requests.models.Response'>
print(type(page_response))
# requests.models.Response
page = BeautifulSoup(page_response.content, 'html.parser')  # <class 'bs4.BeautifulSoup'>
print(type(page))
element = page.find('td', class_='mcnTextContent', style=re.compile('padding-top'), valign='top')
print(type(element))
page_element_iterable = iter(element)

