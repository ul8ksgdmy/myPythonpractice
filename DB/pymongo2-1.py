from pymongo import MongoClient
from pymongo import errors
import json

#접속데이터 호출
def getConnection():
    with open('myinfo.json') as f:
        data = json.load(f)

    host = data['host']
    port = data['port']

    client = MongoClient(host,port)
    #check a connection right by database list
    databaseList = client.list_database_names()
    client.close()

    return databaseList

print(getConnection())