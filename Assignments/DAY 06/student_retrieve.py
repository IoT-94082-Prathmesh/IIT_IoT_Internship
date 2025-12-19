# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="student",      # ✅ correct database
    use_pure=True
)

# SQL query
query = "SELECT * FROM info_students"

# create cursor
cursor = connection.cursor()

# execute query
cursor.execute(query)

# fetch all records
students = cursor.fetchall()

# display records
for student in students:
    print(student)

# close cursor and connection
cursor.close()
connection.close()
