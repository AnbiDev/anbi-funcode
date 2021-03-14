import re
import requests
from bs4 import BeautifulSoup

site = 'https://anbidev.github.io/gallery/'

response = requests.get(site)

tag = 'img'
attr = 'src'

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all(tag) 

urls = [img[attr] for img in img_tags] 
print(urls)

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
        continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)