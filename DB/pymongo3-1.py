#csv 데이터를 호출하여 pymongo에 입력
#DB의 이름은 HR
#collection의 이름은 employees

import json
import datetime
from pymongo import MongoClient

############ 변수
#정보 저장
info = []
infotext = ""

#DB연결
host = ""
port = ""
dbName = ""
colectionName = ""

#외부에 저장한 ip 및 port 가져오기
with open('C:\\Users\W7\python-workspace\myPythonpractice\DB\myinfo.json','r') as f:
    data = json.load(f)

#연결
host = data['host']
port = data['mongoport']

#db and collections
dbName = 'HR'
colectionName = 'employees'

#mongodb에 데이터 저장
#1 mongodb에 연결

client = MongoClient(host=host, port=port)
db = client[dbName]
col = db.get_collection(colectionName)

# salary가 15000이상인 데이터
param = {'SALARY':{'$gt':15000}}
projection = {'EMPLOYEE_ID' : 1, 'SALARY' : 1}
p1 = col.find(param, projection)
for i in p1:
    print('q1 : '+str(i))

# 2005년 1월 1일부터 12월 31일사이의 hire_date 가져오기
start = datetime.datetime(2005, 1, 1, 0, 0)
end = datetime.datetime(2005, 12, 31, 0, 0)
param = {'HIRE_DATE': {'$gte' : start, '$lte' : end}}
projection = {'HIRE_DATE' : 1}
p2 = col.find(param, projection)
for i in p2:
    print('q2 : '+str(i))

# salary의 총합이 10000 ~ 20000 사이인 job id (역순정렬)
param = [{'$group'  :   {'_id' : '$JOB_ID', 'total' : {'$sum': '$SALARY'}}},
         {'$match'  :   {'total':{'$lt':20000,'$gt':10000}} },
         {'$sort'   :   {'total':-1}}]
q3 = col.aggregate(param)
for i in q3:
    print('q3 : '+str(i))



client.close()