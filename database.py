import mysql.connector

def get_data():
    mydb = mysql.connector.connect(host = "localhost", user="root",password="astroboy", database = "testdb")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM students")
    result = mycursor.fetchmany()
    mydb.close()
    return result

