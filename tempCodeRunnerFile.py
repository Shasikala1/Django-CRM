import mysql.connector

dataBase=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Shasiram@143',
    auth_plugin='mysql_native_password'
)
#prepare a cursor object
cursorObject=dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")