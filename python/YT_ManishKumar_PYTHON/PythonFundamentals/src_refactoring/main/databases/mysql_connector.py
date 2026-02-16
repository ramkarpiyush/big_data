from loguru import logger
import mysql.connector
from mysql.connector import Error
import configparser
from src_refactoring.main.encrypt_decrypt.AES_Encryption import decrypt

class MySqlConnection:
    def __init__(self, config):
        self.config = config
        self.connection=None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host = self.config["mysql_database"]["host"],
                                                user = self.config["mysql_database"]["user"],
                                                password = self.config["mysql_database"]["password"] #decrypt(self.config["mysql_database"]["password"])
                                                ,database = self.config["mysql_database"]["database"]
                                                )
            logger.info("MySQL Connection Suucessful.")
        except Exception as e:
            logger.error(f"Error occured: {e}")
            raise e
        
    def closer(self):
        if self.connection.is_connected():
            self.connection.close()
            logger.info("MySQL Connection closed")

class MySqlCrudOperations:
    def  __init__(self, mysql_connection):   
        self.connection = mysql_connection

    def read_from_mysql(self, query):
        logger.info(f"Query sent to read: {query}")
        try:    
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            logger.info(f"{result}")
            return result

        except Exception as e:
            logger.info(f"Error occured in MySQL query run: {e}")
            raise e      
        
        finally:
            if cursor:
                cursor.close()  
                logger.info("Cusrsor closed.")

    def inser_from_mysql(self, query):
        logger.info(f"Query sent Insert the data: {query}")
        try:    
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            logger.info(f"{result}")
            return result

        except Exception as e:
            logger.info(f"Error occured in MySQL query run: {e}")
            raise e     

        finally:
            self.connection.commit()

