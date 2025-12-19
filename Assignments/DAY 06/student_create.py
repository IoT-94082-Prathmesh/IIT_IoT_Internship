# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="student",     # ✅ correct database
    use_pure=True
)

# take input from user
rollno = int(input("Enter rollno : "))
name = input("Enter name : ")
email = input("Enter email : ")
course = input("Enter course : ")

# create a cursor
cursor = connection.cursor()

# parameterized query (BEST PRACTICE)
query = "INSERT INTO info_students VALUES (%s, %s, %s, %s)"
data = (rollno, name, email, course)

# execute query
cursor.execute(query, data)

# commit changes
connection.commit()

print("Record inserted successfully")

# close resources
cursor.close()
connection.close()
