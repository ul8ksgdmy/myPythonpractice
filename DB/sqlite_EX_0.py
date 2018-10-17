import sqlite3

url = 'C:/Users/W7/python-workspace/myPythonpractice/test.db'

#normal conncect
conn = sqlite3.connect(url)

#auto_commit
# conn = sqlite3.connect(url, isolation_level=None)

#cursor
cs = conn.cursor()

# sql = "select * from customer where category=? and region=?"
# cs.execute(sql, (1, 'Sea'))

# # sql = "select * from customer where id = :Id"
# # cs.execute(sql, {"Id": 1})

# for row in cs.fetchall():
#     print(row)

sql = "insert into customer(name,category,region) values (?, ?, ?)"
# cs.execute(sql, ('홍길동', 1, '서울'))

data = (
    ('홍진우', 1, '서울'),
    ('강지수', 2, '부산'),
    ('김청진', 1, '서울'),
)

cs.executemany(sql, data)

#commit
conn.commit()

conn.close()
