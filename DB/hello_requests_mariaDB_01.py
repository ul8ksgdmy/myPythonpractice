import mysql.connector
import requests
import lxml.html

#파이썬에서는 정의 위치가 중요하다.
def makeTnC(mycursor, name, site):
    mycursor.execute("SHOW TABLES like 'testTB'")
    tableExC = int(len(mycursor.fetchall()))
    val = (name, site)
    #테이블이 있으면, 데이터를 채우고
    if int(tableExC) > 0:
        mycursor.execute("insert into testTB (name, site) values (%s, %s)", val)
    #테이블이 없으면, 테이블을 만들고 데이터를 채운다.
    else:
        mycursor.execute("create table testTB (id int auto_increment primary key, name varchar(255), site varchar(255))")
        mycursor.execute("insert into testTB (name, site) values (%s, %s)", val)

# DB접속
host = "13.125.178.188"
user = "root"
passwd = "123456"
database = "homeDB" #homeDB 생성 후

mydb = mysql.connector.connect(
    host = host, user = user,
    passwd = passwd, database = database #homeDB 생성 후
)

mycursor = mydb.cursor()

# 정보수집
url2 = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
res = requests.get(url2)
html = res.text

# 정보해석
root = lxml.html.fromstring(html)

#정보가공 및 저장
for part_html in root.xpath('//td[@class="left"]/a'):
    makeTnC(mycursor, str(part_html.text_content()), str(part_html.get('href')))

mydb.commit()