from urllib.request import urlopen
from urllib.request import HTTPError #500, 404등의 http에러 처리용
from bs4 import BeautifulSoup

#잘 구성된 스크래퍼를 만드려면 예외처리가 필수임. 별5개!
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None #서버나 페이지가 문제를 일으킬 때
    try:
        bs0bj = BeautifulSoup(html.read(), "html.parser")
        title = bs0bj.body.h1
    except AttributeError as e:
        print(e)
        return None #요소나 속성이 문제를 일으킬 때
    return title

url = "http://www.pythonscraping.com/pages/page1.html"
title = getTitle(url)
if title == None:
    print("title couldn't be found")
else:
    print(title)