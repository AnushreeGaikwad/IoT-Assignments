# import mysql connector
import mysql.connector

# create connection with mysql server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)
query = "select * from employee;"
cursor = connection.cursor()
cursor.execute(query)
records = cursor.fetchall() 
print(records)

query = "select * from employee where dept = 'sales';"
cursor = connection.cursor()
cursor.execute(query)
records = cursor.fetchall() 
print(records)


query = "select * from employee order by salary DESC LIMIT 1;"
cursor = connection.cursor()
cursor.execute(query)
records = cursor.fetchall() 
print(records)


query = "select * from employee order by salary ASC LIMIT 1;"
cursor = connection.cursor()
cursor.execute(query)
records = cursor.fetchall() 
print(records)

cursor.close()

connection.close()
