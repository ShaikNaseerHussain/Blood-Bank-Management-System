# To check if the connection is successful

from config import get_db_connection

conn = get_db_connection()
if conn.is_connected():
    print("Database connection successful")
else:
    print("Database connection failed")

conn.close()
