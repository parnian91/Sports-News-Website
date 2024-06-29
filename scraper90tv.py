import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
req = requests.get('https://top90.ir/news/')

# Parse the webpage content
content = BeautifulSoup(req.content, 'html.parser')

# Find all h2 tags
heading = content.find_all('h2')

# Print the headings
for header in heading:
    print(header.get_text())
