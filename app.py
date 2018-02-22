from urllib.request import urlopen
from bs4 import BeautifulSoup

# Moving forward:
#  Build an array using the values that we extract
#  Deliver that array to a Vue Interface to modify the display
#  Store scraped data in a database
#  
# Remember 
#  dont go overboard on my calls! No more than 1 a second! :U
#  Only scrape from sites that allow their data to be scraped in their terms 

# Documentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all

# Look into a scraping framework like Scrapy!
# https://doc.scrapy.org/en/1.5/intro/overview.html

#toscrape.com is a really good resource for learning scraping!
page_url = "http://quotes.toscrape.com/tag/inspirational/"

page = urlopen(page_url)

soup = BeautifulSoup(page, 'html.parser')

quoteArray = []
quotes = soup.find_all('span', attrs={'class': 'text'})

for x in quotes:
    quoteArray.append(x.text)

print(quoteArray)