import mysql.connector
import requests
import lxml.html
import json

#파이썬에서는 정의 위치가 중요하다.
def makeTnC(mycursor, name, site):
    mycursor.execute("SHOW TABLES like 'testTB1'")
    tableExC = int(len(mycursor.fetchall()))
    val = (name, site)
    #테이블이 있으면, 데이터를 채우고
    if int(tableExC) > 0:
        mycursor.execute("insert into testTB1 (name, site) values (%s, %s)", val)
    #테이블이 없으면, 테이블을 만들고 데이터를 채운다.
    else:
        mycursor.execute("create table testTB1 (id int auto_increment primary key, name varchar(255), site varchar(255))")
        mycursor.execute("insert into testTB1 (name, site) values (%s, %s)", val)


#myinfo의 개인정보를 이용하여 DB연결.
with open('C:/Users/W7/python-workspace/myPythonpractice/sql/myinfo.json') as f:
    data = json.load(f)

# myinfo.json 양식
# {
#     "host" : "write ip without port",
#     "user" : "write user",
#     "passwd" : "write password",
#     "database" : "write database"
# }

host = data['host']
user = data['user']
passwd = data['passwd']
database = data['database']

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
    #공백확인 후 주석처리 함.
    # k = str(part_html.get('href')).split()
    # if len(k) > 0:
    #     print(k)
        
    # print(part_html.text_content().strip())
    makeTnC(mycursor, str(part_html.text_content()), str(part_html.get('href')))

mydb.commit()