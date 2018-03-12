import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

page_url = "https://www.reddit.com/user/shitty_watercolour/comments/"

headers = {
    'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

page = requests.get(page_url, timeout=5, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

commentArray = []
comments = soup.find_all('div', attrs={'class': 'CommentListing__comment'})

for x in comments:
    commentArray.append(x.find('a')['href'])

print(commentArray)
