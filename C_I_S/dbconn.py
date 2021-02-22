#!C:/Users/Kushang Darbar/AppData/Local/Programs/Python/Python38-32/python
print()
import cgi
import mysql.connector

db = mysql.connector.connect(
  host="project.cogswrata7ds.ap-south-1.rds.amazonaws.com",
  user="admin",
  password="admin1234",
  database="Project"
)
cursor = db.cursor()
if(db):
	print("database connected")

else:
	print("database not connected")
