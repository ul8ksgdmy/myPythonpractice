from urllib.request import urlopen
from urllib.request import HTTPError #500, 404등의 http에러 처리용
from bs4 import BeautifulSoup

#잘 구성된 스크래퍼를 만드려면 예외처리가 필수임. 별5개!
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None #서버나 페이지가 문제를 일으킬 때
    try:
        bs0bj = BeautifulSoup(html.read(), "html.parser")
        nameList = bs0bj.findAll("span",{"class":"green"})
        nameOutput = []
        for name in nameList:
            nameOutput.append(name)
    except AttributeError as e:
        return None #요소나 속성이 문제를 일으킬 때
    return nameOutput

url = "http://www.pythonscraping.com/pages/warandpeace.html"
tNames = getTitle(url)
if tNames == None:
    print("title couldn't be found")
else:
    for html_full in tNames:
        # print(html_full.get_text()) #get_text() or text는 태그 삭제
        print(html_full)
        