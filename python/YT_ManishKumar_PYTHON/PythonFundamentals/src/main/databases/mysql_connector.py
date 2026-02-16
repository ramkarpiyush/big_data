from loguru import logger
import mysql.connector
from mysql.connector import Error
import configparser, os
from src.main.encrypt_decrypt.AES_Encryption import decrypt

def read_from_mysql(config, query):
    try:    
        db_user = os.getenv("DB_USER")
        connection = mysql.connector.connect(host = config["mysql_database"]["host"],
                                                user = db_user, #config["mysql_database"]["user"],
                                                password = decrypt(config["mysql_database"]["password"]))

        logger.info(f"{connection}")

        cursor = connection.cursor()
        
        cursor.execute(query)
        result = cursor.fetchall()
        logger.info(f"{result}")
        logger.info("Query done in the database")
        return result

    except Exception as e:
        logger.info(f"Error occured in MySQL DB {e}")
        raise e
    
    finally:
        connection.close()
        cursor.close()