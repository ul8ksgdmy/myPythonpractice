import urllib.request as ur
from bs4 import BeautifulSoup as bs

#get response
url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'
res = ur.urlopen(url)

#parsing
soup = bs(res, 'html.parser')

# show me
for poem in soup.select('#mw-content-text > div > ul > li a'):
    print(poem.string)