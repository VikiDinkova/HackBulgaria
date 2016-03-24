from collection import deque
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

base_url = 'http://register.start.bg/'
links = deque()
links.append(base_url)
visited = set()

while len(links) > 0:
    link = links.pop()
    visited.add(link)
    r = requests.get(link)
    html = r.text
    msg = link
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all('a'):
        if tag.get('href') is not None and '#' not in tag.get('href'):
            tag = tag.get('href')
            if 'http' in tag:
                links.append(tag)
            else:
                tag = urljoin(msg, tag)
                links.append(tag)



# for item in visited:
#     r = requests.get(item, verify=False, timeout=5)
#     print(r.headers["Server"])
