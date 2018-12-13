from pymongo import MongoClient
from pymongo import errors
import json

#접속데이터 호출

# myinfo.json
# {
#     "host" : [ip],
#     "port" : [port],
#     "database" : "mongodb",
#     "collection" : "restaurants"
# }

# 같은 경로에 myinfo.json을 둘 것.
with open('myinfo.json') as f:
    data = json.load(f)

j_host = data['host']
j_port = data['port']
j_database = data['database']
j_collection = data['collection']

client = MongoClient(j_host,j_port)
#check a connection right by database list
# databaseList = client.list_database_names()

#데이터를 받아오면 vscode가 변수를 인식하지 못함.
# database = client[j_database]
# collection = database[j_collection]

#그래서 직접 db와 collection을 입력
database = client['mongodb']
collection = database['restaurants']

#query
query = {'address.street' : 'Tompkins Avenue'}

#option
sort = [('_id',-1)]

cursor = collection.find(query,sort=sort, limit=1000)

try :
    for doc in cursor:
        print(doc)
finally:
    cursor.close()