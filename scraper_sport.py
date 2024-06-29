import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
req = requests.get('https://www.varzesh3.com/')

# Parse the webpage content
content = BeautifulSoup(req.content, 'html.parser')


# Find all h3 tags within a tags with class "title"
a_tags = content.find_all('a', {'class':'title'})
for a_tag in a_tags[0:8]:
    h3_tag = a_tag.find('h3')
    if h3_tag:
        h3_content = h3_tag.text
        print(h3_content)
