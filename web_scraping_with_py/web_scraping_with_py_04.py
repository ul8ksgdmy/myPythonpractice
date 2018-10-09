#케빈베이컨 페이지 스크래핑
from urllib.request import urlopen
from urllib.request import HTTPError #500, 404등의 http에러 처리용
from bs4 import BeautifulSoup
import re

def linkScraper(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    #div 태그의 bodyContent 중 a 태그에서 /wiki로 시작하고 세미콜론이 안 들어가는 항목을 찾음.
    for link in bs.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])

linkScraper('https://en.wikipedia.org/wiki/Kevin_Bacon')

        