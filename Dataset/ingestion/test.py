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
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = %s
                ORDER BY table_name;
            """, (DB_NAME,))

            rows = cur.fetchall()
            if not rows:
                print(f"No tables found in database '{DB_NAME}'.")
            else:
                print(f"Tables in '{DB_NAME}':")
                for (table_name,) in rows:
                    print(f" - {table_name}")

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
        # conn wasn't created
        pass


# import mysql.connector

# try:
#     with mysql.connector.connect(
#         host="localhost",
#         dbname="postgres",
#         user="postgres",
#         password="postgres"
#     ) as conn:
        
#         with conn.cursor() as cur:
#             cur.execute("""
#                 SELECT table_name
#                 FROM information_schema.tables
#                 WHERE table_schema = 'myschema';
#             """)
            
#             for row in cur.fetchall():
#                 print(row[0])

# except Exception as e:
#     print("Error:", e)