import mysql.connector

def get_data():
    mydb = mysql.connector.connect(host = "localhost", user="root",password="astroboy", database = "testdb")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM studentss")
    result = mycursor.fetchmany()
    mydb.close()
    return result

