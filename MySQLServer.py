import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="pass"
    )
except Exception as db_connection_err:
    print(f"Couldn't connect to Database: {db_connection_err}")
    exit()

cursor = mydb.cursor()

try:
    cursor.execute("CREATE DATABASE alx_book_store;")
except Exception as db_creation_err:
    print(f"Error creating database: {db_creation_err}")

print(f"Database 'alx_book_store' created successfully!")

cursor.close()
mydb.close()


