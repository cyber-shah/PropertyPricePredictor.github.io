import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "aH24fkWu*}Q",
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE miami_housing")

print("Database created successfully")