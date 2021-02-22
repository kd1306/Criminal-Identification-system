#!C:/Users/Kushang Darbar/AppData/Local/Programs/Python/Python38-32/python
print()
import cgi


#import mysql.connector

#mydb = mysql.connector.connect(
 # host="localhost",
  #user="yourusername",
  #password="yourpassword",
  #database="mydatabase"
#)

#mycursor = mydb.cursor()

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

import pymysql

def insertData(data):
    rowId = 0

    db = pymysql.connect("project1.cogswrata7ds.ap-south-1.rds.amazonaws.com", "admin", "admin1234", "project")
    cursor = db.cursor()
    print("database connected")

    query = "INSERT INTO register VALUES('%s', '%d', '%s', '%s', '%d', '%d');" % \
            (data["Name"], data["age"], data["Dob"], data["Crime_Commited"],
             data["punishment_duration"], data["Photo"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")


    db.close()
    print("connection closed")
    return rowId
