#!C:/Users/Kushang Darbar/AppData/Local/Programs/Python/Python38-32/python
#print("Content-Type:text/html; charset=utf-8")
print()
import cgi
import pymysql

def retrieveData(predicted_name):
    id = None
    crim_data = None

    db = pymysql.connect("rds-covid19.cgtgaqfkiucx.ap-south-1.rds.amazonaws.com", "admin", "Bijapur!!08", "dbname")
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM register WHERE Name='%s'"%predicted_name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id=result[0]
        crim_data = {
            "Name" : result[1],
            "Age" : result[2],
            "Dob" : result[3],
            "Crime_Commited" : result[4],
            "punishment_duration" : result[5],
            "photo" : result[6],            
        }
        print("data retrieved")
        print("Name:",result[1])
        print("Age:", result[2])
        print("Dob:", result[3])
        print("Crime_Commited:", result[4])
        print("punishment_duration:", result[5])
        #print("photo:", result[6])
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, crim_data)
