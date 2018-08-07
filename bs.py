from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup

def google_scrape(url):
    try:
        thepage = urllib.request.urlopen(url)
        soup = BeautifulSoup(thepage, "html.parser")
        return soup.title.text
    except:
        return " "
    

i = 1
count = 1;
query = 'roses '
for url in search(query):
    a = google_scrape(url)
    #if (b/100 >=4 ):
        # res = a
        # print(url)
    count = count +1;
    if (count>10):
        break
    # print str(i) + ". " + a
    print(a)
    print (url)
    print (" ")

# from bs4 import BeautifulSoup
# from googlesearch import search
# import google
# import urllib.request
# from urllib.parse import quote

# search_item = "cat"
# url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
# print(url)
# content = urllib.request.urlopen(url)



# soup = BeautifulSoup(content, 'html.parser')
# print (soup.prettify())
#for link in soup.find_all('a'):
#  print(link.get('href'))
#2
# import urllib
# from bs4 import BeautifulSoup
# import requests
# import webbrowser

# text = 'hello world'
# text = urllib.parse.quote_plus(text)

# url = 'https://google.com/search?q=' + text

# response = requests.get(url)

# #with open('output.html', 'wb') as f:
# #    f.write(response.content)
# #webbrowser.open('output.html')

# soup = BeautifulSoup(response.text, 'html.parser')
# for g in soup.find_all('a'):
#     print(g)
#     print('-----')
# print (soup.prettify())

# def google_scrape(url):
#     thepage = urllib.request.urlopen(url)
#     soup = BeautifulSoup(thepage, "html.parser")
#     return soup.find_all('a')
#     # return soup.title.text

# i = 1
# query = 'where to find cat'
# for url in search(query, stop=5):
#     a = google_scrape(url)
#     print (str(i) + ". " + a)
#     print (url)
#     print (" ")
#     i += 1


# import GoogleScraper
# import urllib.parse

# if __name__ == '__main__':

#     results = GoogleScraper.scrape('Best SEO tool', num_results_per_page=50, num_pages=3, offset=0)
#     for page in results:
#         for link_title, link_snippet, link_url in page['results']:
#             # You can access all parts of the search results like that
#             # link_url.scheme => URL scheme specifier (Ex: 'http')
#             # link_url.netloc => Network location part (Ex: 'www.python.org')
#             # link_url.path => URL scheme specifier (Ex: ''help/Python.html'')
#             # link_url.params => Parameters for last path element
#             # link_url.query => Query component
#             try:
#                 print(urllib.parse.unquote(link_url.geturl())) # This reassembles the parts of the url to the whole thing
#             except:
#                 pass

# # How many urls did we get on all pages?
# print(sum(len(page['results']) for page in results))

# # How many hits has google found with our keyword (a
