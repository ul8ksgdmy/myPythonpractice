from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sqlite3

#DB연결
dbpath = 'test.sqlite'
conn = sqlite3.connect(dbpath)
cs = conn.cursor()

#table 생성
#이스케이프 코드를 쓰지 않고 문장을 쓰기 위해 따옴표3개로 처리함
cs.executescript("""
/* 테이블제거 */
drop table if exists movie;

/* 테이블 생성 */
create table movie(
    id integer primary key autoincrement,
    title text
);
""")

#selenium은 requests의 역할을 하는 것. 나머지는 같다.

#브라우저 실행
firefox = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')

#경로지정 및 접속
url = 'https://movie.daum.net/main/new#slide-1-0'
####requests와의 차이 response로 온 html을 보기 위해서는 page_source를 이용
firefox.get(url)
firefox.refresh()
res = firefox.page_source 
# 확인 # print(firefox.page_source)
#parsing
soup_html = BeautifulSoup(res, 'lxml')

titlelist = []
#insert DML준비
sql = 'insert into movie(title) values(?)'

for i in range(4):

    time.sleep(3)
    #사전작업 : 클릭할 'element'를 준비
    slide = firefox.find_element_by_id('mainSlideNextBtn')
    #사전작업 : action준비
    mouse = webdriver.ActionChains(firefox)
    
    #액션이 일어날 element로 포인트를 이동하여 action.
    mouse.move_to_element(slide).click().perform()
    for j in soup_html.select('strong.tit_poster > a'):
        # 튜플 자료형 때문에 개고생
        # 아래와 같이 튜플 형태로 지정해야 execute명령어가 실행됨.
        x = (j.text,)
        cs.execute(sql, x)
        titlelist.append(x)
        # 확인 print(j.text)

#리스트 형태로 넣을 경우.
# cs.executemany(sql, titlelist)

conn.commit()

firefox.close()