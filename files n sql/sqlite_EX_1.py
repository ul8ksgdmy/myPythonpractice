import sqlite3
 
conn = sqlite3.connect("test.db")
 
#with는 에러가나도 리소스를 닫기 때문에 DB를 사용할 때 쓰면 좋음.
with conn:
    cur = conn.cursor()
    cur.execute("select * from customer")
    rows = cur.fetchall()
 
    for row in rows:
        print(row)