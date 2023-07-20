import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)
mycursor = mydb.cursor()
sql="DROP TABLE IF EXISTS customer"
mycursor.execute(sql)


