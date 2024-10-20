import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="pass"
    )
except mysql.connector.Error as db_connection_err:
    print(f"Couldn't connect to Database: {db_connection_err}")
    exit()

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
print(f"Database 'alx_book_store' created successfully!")

cursor.close()
mydb.close()


