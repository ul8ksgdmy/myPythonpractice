#케빈베이컨 페이지 스크래핑
from urllib.request import urlopen
from urllib.request import HTTPError #500, 404등의 http에러 처리용
from bs4 import BeautifulSoup
import re
import datetime
import random
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bs = BeautifulSoup(html, "html.parser")
    return bs.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)