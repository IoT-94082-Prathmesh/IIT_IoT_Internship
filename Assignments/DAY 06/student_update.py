# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="student",
    use_pure=True
)

# take input
name = input("Enter name whose email to be updated : ")
email = input("Enter new email : ")

# create cursor
cursor = connection.cursor()

# parameterized UPDATE query
query = "UPDATE info_students SET email = %s WHERE name = %s"
data = (email, name)

# execute query
cursor.execute(query, data)

# commit changes
connection.commit()

print(cursor.rowcount, "record(s) updated")

# close resources
cursor.close()
connection.close()
