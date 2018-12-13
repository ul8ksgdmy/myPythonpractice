#mongodb접속
#csv호출
#mongoDB에 맞는 Dictionary type으로 변경
#mongodb에 저장

from pymongo import MongoClient
from collections import OrderedDict

import csv
import json

with open('PATH') as f:
    data = json.load(f)

host = data['host']
port = data['port']

client = MongoClient(host,port)

#HR DB 만들기
dbName = 'HR'
colName = 'EMPLOYEES'

#DB가 있으면 지우고
# if dbName in client.list_database_names():
if len(client.get_database(dbName).list_collection_names()) > 0:
    client.drop_database(dbName)
#없으면 바로 collection을 만듦
col = client[dbName].create_collection(colName)


#csv호출
f = open('PATH','r')
csvdata = csv.DictReader(f)

#keynames
keyNames = csvdata.fieldnames
for values in csvdata:
    # keyNames에 해당하는 values를 저장할 newDict 선언
    newDict = {}
    for j in keyNames:
        newDict[j] = values[j]
    # 한 턴의 newDict을 바로 mongoDB에 저장
    insert = col.insert_one(newDict)
    print(insert.inserted_id)
f.close()
client.close()