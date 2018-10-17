import pymysql
import json

# myinfo.json 양식
# {
#     "host" : "write ip without port",
#     "user" : "write user",
#     "passwd" : "write password",
#     "database" : "write database"
# }

# data = []
path = 'C:/Users/W7/python-workspace/myPythonpractice/files n sql/myinfo.json'
with open(path) as f:
    data = json.load(f)
    #class 확인
    print(type(data))

host = data['host']
user = data['user']
password = data['passwd']
db = data['database']

# MySQL Connection 연결
conn = pymysql.connect(host=host, user=user, password=password,db=db, charset='utf8')
 
# Connection 으로부터 Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)
 
# SQL문 실행
sql = "select * from customers where id=%s and address=%s"
curs.execute(sql, (9, 'one way 98'))
 
# 데이타 Fetch
rows = curs.fetchall()
for row in rows:
    #dictionary형태로 데이터 출력 만약 dictionary cursor가 아니었으면 튜플 출력
    # 출력비교
    # conn.cursor(pymysql.cursors.DictCursor)의 경우
    # {'name': 'Susan', 'address': 'One way 98', 'id': 9}
    # conn.cursor()의 경우
    # ('Susan', 'One way 98', 9)
    print(row)
    #dictionary형태이기 때문에 아래와 같은 print가 가능
    print(row['id'], row['name'], row['address'])
 
# Connection 닫기
conn.close()