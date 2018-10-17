#mongoDB로부터 특정 자료를 호출하여
#Sqlite에 저장하는 프로그램

from pymongo import MongoClient
import sqlite3
import json

with open('myinfo.json') as f:
    data = json.load(f) 

host = data['host']
port = data['mongoport']

client = MongoClient(host,port)
db = client.get_database('mongodb')
collection = db.get_collection('restaurants')

query = {'address.street' : 'Morris Park Ave'}
param = {'_id':False, 'adress.street':True}
print(collection.find(query).count())
cs = collection.find(query,param)

for i in cs:
    print(i[2])

client.close()