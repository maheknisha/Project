

import mysql.connector
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="route",
        password="MySql@1234"
        database="ecommerce"
    )
if __name__ == "__main__":
    try:
        db = get_db()
        print("Database connected successfully")
        db.close()
    except Exception as e:
        print("Database connection failed:",e)
