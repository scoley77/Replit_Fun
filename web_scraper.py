# http://www.dailysmarty.com/topics/python
# only urls going straight to a post
# convert url to title
# requests, inflection, beautifulsoup

# use requests and soup to grab post urls, use inflection to reformat the urls into post titles
# when calling a function inside a function, store it in a variable, so that the return value can be used easily

# import requests
# import inflection
# from bs4 import BeautifulSoup

# urls = ['http://www.dailysmarty.com/topics/python', 'http://www.dailysmarty.com/topics/python?page=2', 'http://www.dailysmarty.com/topics/python?page=3', 'http://www.dailysmarty.com/topics/python?page=4']

# def title_generator(title_list):
#   titles = scraper(title_list)
#   for title in titles:
#     print(title)

# def scraper(list):
#   titles = []

#   def format(link):
#     title = link.replace('/posts/', '')
#     return inflection.titleize(title)

#   for url in list:
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     links = soup.find_all('a')
#     for link in links:
#       unformatted = str(link.get('href'))
#       if '/posts/' in unformatted:
#         title = format(unformatted)
#         titles.append(title)
#       else:
#         continue
#   return titles

# title_generator(urls)