from pymongo import MongoClient

# configure connection
conn = MongoClient('127:0:0:0',1) #write ip and port

#creating a collection
mydb = conn['pydb']
mycol = mydb['customers']

# check if my db exits
print('database names : ', end="")
print(conn.list_database_names())

# specify a db to connect
if mycol == '':
    dbName = 'hellomongo'
else:
    dbName = 'pydb'
    #Since a collection is not created until it gets content in MongoDB, put data into the collection to try to make.
    mydict = { "name": "John", "address": "Highway 37" }
    mydicts = [
                { "name": "Amy", "address": "Apple st 652"},
                { "name": "Hannah", "address": "Mountain 21"},
                { "name": "Michael", "address": "Valley 345"},
                { "name": "Sandy", "address": "Ocean blvd 2"},
                { "name": "Betty", "address": "Green Grass 1"},
                { "name": "Richard", "address": "Sky st 331"},
                { "name": "Susan", "address": "One way 98"},
                { "name": "Vicky", "address": "Yellow Garden 2"},
                { "name": "Ben", "address": "Park Lane 38"},
                { "name": "William", "address": "Central st 954"},
                { "name": "Chuck", "address": "Main Road 989"},
                { "name": "Viola", "address": "Sideway 1633"}
            ]
    sg = mycol.insert_one(mydict) #insert a record (or a document as it is called in MongoDB)
    mt = mycol.insert_many(mydicts) #insert multiple documents
    print('inserted id : ' + str(sg.inserted_id))
    print('inserted ids : ' + str(mt.inserted_ids))

db = conn.get_database(dbName)

#check if a list of collections exists
collection_list = db.list_collection_names()

# use print to return a list of my collection
# choose one below which you prefer
print('collection names : ', end="")
print(collection_list)
# for list in collection_list:
#     print(list)

# specify a collection to connect
colName = 'article'
collection = db.get_collection(colName)


