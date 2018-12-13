#csv 데이터를 호출하여 pymongo에 입력
#DB의 이름은 HR
#collection의 이름은 employees

import csv
import json
import time
import datetime
from collections import OrderedDict
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

#to save data from csv
csvdata = OrderedDict()

#mongodb에 넣을 데이터용 list 생성
arowData = []

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

#DB 생성
if dbName in client.database_names():
    client.drop_database(dbName)
    time.sleep(1)    
db = client[dbName]

#collection 생성
if colectionName in db.list_collection_names():
    col = db.get_collection(colectionName)
    
else:
    col = db.create_collection(colectionName)

#데이터 호출
fcsv = open('C:\\Users\W7\python-workspace\myPythonpractice\EMPLOYEES.csv','r')
csvdata = csv.DictReader(fcsv)

#데이터 호출 확인
if len(csvdata.fieldnames) > 0:
    infotext = '데이터 호출 확인 :' + 'yes'
else:
    infotext = '데이터 호출 확인 :' + 'no'
info.append(infotext)

#저장 csv > database 

for csvdata_in_a_row in csvdata:
    #db에서 쓸 각 필드의 이름은 csv와 동일
    #employees의 fieldnames 호출 (그러니까 여기 for문은 데이터 한 줄)
    dbdic = {}
    for i in csvdata.fieldnames:
        if i == 'HIRE_DATE': #특이사항 1 : hire data - date
            timeformat = '%Y-%m-%d'
            dbdic[i] = datetime.datetime.strptime(csvdata_in_a_row[i], timeformat)
        elif i == 'SALARY': #특이사항 2 : salary - int
            dbdic[i] = int(csvdata_in_a_row[i])
        elif i == 'COMMISSION_PCT': #특이사항 3 : commision - float
            if csvdata_in_a_row[i] != '': #빈 칸이 아닐 경우
                dbdic[i] = float(csvdata_in_a_row[i])
            else: #빈 칸일 경우 0.0
                dbdic[i] = float(0) 
        else:
            dbdic[i] = csvdata_in_a_row[i]
    #save data in the list
    arowData.append(dbdic)
#파일 사용 끝
fcsv.close()

#insert data into db from the list
for i in arowData:
    insertdb = col.insert_one(i)
    print(insertdb.inserted_id)

client.close()