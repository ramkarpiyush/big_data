import mysql.connector
from mysql.connector import Error

DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"         # change if different
DB_PASSWORD = "12345678"  # change accordingly
DB_NAME = "gdb041"      # e.g., 'sakila' or any DB you created

try:
    # Establish connection
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,   # for MySQL use 'database', not 'dbname'
        autocommit=True
    )

    if conn.is_connected():
        print(f"Connected to MySQL -> {DB_HOST}:{DB_PORT}, database='{DB_NAME}'")
        with conn.cursor() as cur:
            # List tables in the current database
            cur.execute("""
                SHOW TABLES;
            """)

            rows = cur.fetchall()
            # print(rows)

            table_list = []

            for row in rows:
                # print(row[0])
                table_list.append(row[0])

            print(table_list)

except Error as e:
    print("MySQL Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    try:
        if conn and conn.is_connected():
            conn.close()
            print("Connection closed.")
    except NameError:
        pass

