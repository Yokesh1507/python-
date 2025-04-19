import mysql.connector

# connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",        # or use "127.0.0.1"
    user="root",             # your MySQL username
    password="1507",  # your MySQL password
    database="hostel"   # database name (optional at first)
)

# check if connection successful
if mydb.is_connected():
    print("✅ Connected to MySQL successfully!")
else:
    print("❌ Connection failed.")
