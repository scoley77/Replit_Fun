# http://www.dailysmarty.com/topics/python
# only urls going straight to a post
# convert url to title
# requests, inflection, beautifulsoup

# use requests and pprint to grab post urls, use inflection to reformat the urls into post titles, 
import requests
import inflection
from bs4 import BeautifulSoup

urls = ['http://www.dailysmarty.com/topics/python', 'http://www.dailysmarty.com/topics/python?page=2', 'http://www.dailysmarty.com/topics/python?page=3', 'http://www.dailysmarty.com/topics/python?page=4']
for url in urls:
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find(class_='card')
  cards = results.find_all('div', class_='post-link-title')
  for card in cards:
    post_title = card.find("h2")
    for link in post_title:
      link = post_title.find("a")
      for post_url in link:
        post_url = str(link.get("href"))
        title = post_url.replace('/posts/', '')
        print(inflection.titleize(title))