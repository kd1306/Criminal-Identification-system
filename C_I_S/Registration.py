#!C:/Users/Kushang Darbar/AppData/Local/Programs/Python/Python38-32/python
#print("Content-Type:text/html; charset=utf-8")
print()
import cgi
#import requests
import mysql.connector
#import dbconn
form = cgi.FieldStorage()
Name=form.getvalue('name')
Age=form.getvalue('age')
Dob=form.getvalue('Dob')
Crime_Commited=form.getvalue('Crime_Commited')
punishment_duration=form.getvalue('punishment_duration')
photo=form.getvalue('Photo')
#def form():

#if(requests == 'POST'):
#    Name=requests.form['name']
#    Age=request.form['age']
#    Dob=request.form['Dob']
#    Crime_Commited=request.form['Crime_Commited']
#    punishment_duration=request.form['punishment_duration']
#    photo=request.form['Photo']
#print(Name,Age,Dob,Crime_Commited,punishment_duration,photo)
#    return 
#form();
#def insertData():
rowId = 0

db = mysql.connector.connect(host="rds-covid19.cgtgaqfkiucx.ap-south-1.rds.amazonaws.com", user="admin", password="Bijapur!!08", database="dbname")
cursor = db.cursor()
print("database connected\n")
#    query = "INSERT INTO register (Name, Age, Dob, Crime_Commited, punishment_duration, photo) VALUES(%s, %s, %s, %s, %s, %s)"
#    val = (data["Name"], data["Age"], data["Dob"], data["Crime_Commited"], data["Punishment_duration"], data["Photo"])
#    print(val)
try:
    query = "INSERT INTO register (Name, Age, Dob, Crime_Commited, punishment_duration, photo) VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (Name,Age,Dob,Crime_Commited,punishment_duration,photo))
    db.commit()
    rowId = cursor.lastrowid
    print("data stored on row %d\n" % rowId)

except:
    db.rollback()
    print("Data insertion failed\n")


db.close()
print("connection closed")
#return rowId


#insertData();