import mysql.connector

host = "13.125.178.188"
user = "root"
passwd = "123456"
database = "homeDB" #homeDB 생성 후

mydb = mysql.connector.connect(
    host = host, user = user,
    passwd = passwd, database = database #homeDB 생성 후
)

mycursor = mydb.cursor()

# mycursor.execute("create database homeDB") #1
# mycursor.execute("show databases")

# mycursor.execute("create table customers (name varchar(255), address varchar(255))") #2
# mycursor.execute("show tables")

# mycursor.execute("alter table customers add column id int auto_increment primary key") #3
# mycursor.execute("show columns from customers")

#insert
# insertCommand = "insert into customers (name, address) values (%s, %s)"
# sql = insertCommand
# val = ("John", "Highway 21") #4-1

# mycursor.execute(sql, val) #단일 데이터를 처리할 때

# val = [                       #4-2
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val) #다수의 데이터를 처리할 때

# 공통
# mydb.commit() #Important!: Notice the statement: mydb.commit().
# #It is required to make the changes, otherwise no changes are made to the table.


#select
# selectCommand1 = "select * from customers where address like %s" #5-1
# sql = selectCommand1
# adr = ("%way%",) #튜플에서는 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다는 것
# mycursor.execute(sql, adr)

#delete
# deleteCommand1 = "delete from customers where address like %s" #6-1
# sql = deleteCommand1
# adr = ("Mountain 21",)
# mycursor.execute(sql, adr)

#update
updateCommand1 = "update customers set address = %s where address = %s"
sql = updateCommand1
adr = ('Valley 345','Canyon 123')
mycursor.execute(sql, adr)
mydb.commit()

print(mycursor.rowcount, "record updated")
# print("1 record inserted, ID : ", mycursor.lastrowid)


# for i in myresult:
#     print(i)

