import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="student"
)

cursor = connection.cursor()

rollno = int(input("Enter rollno : "))
name = input("Enter name : ")
email = input("Enter email : ")
course = input("Enter course : ")

query = """
INSERT INTO students (rollno, name, email, course)
VALUES (%s, %s, %s, %s)
"""

cursor.execute(query, (rollno, name, email, course))
connection.commit()

print("Record inserted successfully")

cursor.close()
connection.close()
