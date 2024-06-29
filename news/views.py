from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
req = requests.get('https://top90.ir/news/')

# Parse the webpage content
content = BeautifulSoup(req.content, 'html.parser')

# Find all h2 tags
heading = content.find_all('h2')

# Print the headings
news = []
for header in heading:
    news.append(header.get_text())
    
##################################################################    
    
# Send a GET request to the webpage
req_n = requests.get('https://www.varzesh3.com/')

# Parse the webpage content
cont = BeautifulSoup(req_n.content, 'html.parser')

# Find all h3 tags within a tags with class "title"
v_news = []
a_tags = cont.find_all('a', {'class':'title'})
for a_tag in a_tags[0:10]:
    h3_tag = a_tag.find('h3')
    if h3_tag:
        h3_content = h3_tag.text
        v_news.append(h3_content)
        
#######################################################
def index(request):
    return render(request, 'news/index.html', {'news':news, 'v_news':v_news})
    
