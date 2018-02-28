import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

page_url = "http://127.0.0.1:8082/more-interesting.html"

headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

page = requests.get(page_url, timeout=5, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

testArray = []
item = {}
tests = soup.find_all('li', attrs={'class': 'card'})

for x in tests:
    item = {
        'name': x.find('span', attrs={'class': 'title'}).text
        , 'description': x.find('span', attrs={'class': 'description'}).text
    }
    testArray.append(item['name'] + ' - ' + item['description'])

print("\n".join(testArray))