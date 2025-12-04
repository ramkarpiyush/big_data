from loguru import logger
import mysql.connector
from mysql.connector import Error

#connection = None

try:
    connection = mysql.connector.connect(host = "localhost",
                                         user = "root",
                                         password = "12345678")
    
    if connection.is_connected():
        logger.info("Connection to MySQL was successful...")
    else:
        logger.error("Failed to connect")

except Error as e:
    logger.error(str(e))

except Exception as e:
    logger.error(type(e).__name__)

'''
finally:
    if connection.is_connected():
        connection.close()
        logger.info("MySQL connection is closed...")
    else:
        logger.info("No open connection to close")
'''

'''
# Cursor:
A cursor is an object that acts as a control structure to interact with the database. 

It allows you to:
- Send SQL queries to the database.
- Fetch results from those queries.
- Iterate through rows returned by a SELECT statement.

Working:
When you connect to a database using a connector (like mysql-connector-python), you get a connection object. 
From that connection, you create a cursor:
'''

cursor = connection.cursor()
cursor.execute("select customer_code, market from gdb041.dim_customer limit 10")
result = cursor.fetchall()
logger.info(f"{result}")
