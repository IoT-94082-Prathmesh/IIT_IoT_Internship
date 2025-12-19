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

# take input
rollno = int(input("Enter rollno of a student to be deleted : "))

# create cursor
cursor = connection.cursor()

# parameterized DELETE query
query = "DELETE FROM info_students WHERE rollno = %s"
data = (rollno,)

# execute query
cursor.execute(query, data)

# commit changes
connection.commit()

# show result
print(cursor.rowcount, "record(s) deleted")

# close resources
cursor.close()
connection.close()
