import requests
import Flask
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

# https://hackernoon.com/web-scraping-tutorial-with-python-tips-and-tricks-db070e70e071

page_url = "http://quotes.toscrape.com/tag/inspirational/"

headers = {
    'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

page = requests.get(page_url, timeout=5, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

quoteArray = []
quotes = soup.find_all('span', attrs={'class': 'text'})

for x in quotes:
    quoteArray.append(x.text)

print(quoteArray)
