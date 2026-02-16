from loguru import logger
from src_refactoring.main.databases.mysql_connector import MySqlConnection, MySqlCrudOperations
from src_refactoring.main.main import *
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"

    def print_details(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email}"

class Labour(Person):
    # total_cnt = 0
    def __init__(self, first_name, last_name, wage, role, crud):
        super().__init__(first_name, last_name)
        # self.first_name = first_name
        # self.last_name = last_name
        self.wage = wage
        self.role = role
        self.crud = crud
        self.id = self.__save_to_database(self.crud)
        # self.check_for_email(crud)
        # Labour.total_cnt += 1

    def __save_to_database(self, crud):
        query = f"select id from home.labours where lower(first_name) = '{self.first_name}' and lower(last_name) = '{self.last_name}';"
        # logger.info(f"Crud: {crud}")
        result = crud.read_from_mysql(query)

        if result:
            logger.info(f"Labout already exists with ID: {result[0][0]}")
            return result[0][0]
        
        # email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"
        logger.info(f"{self.email}")

        insert_query = f"""
            INSERT INTO labours (first_name, last_name, wage, role, email)
            values ('{self.first_name}', '{self.last_name}', {self.wage}, '{self.role}', '{self.email}')
        """
        # logger.info(f"INSERT QUERY: {insert_query}")

        crud.inser_from_mysql(insert_query)

        result = crud.read_from_mysql(query)
        logger.info(f"New labour added with ID: {result[0][0]}")
        return result[0][0]
    
    @staticmethod
    def login_and_logout(crud, id=None, first_name=None, last_name=None):
        if id is None:
            if first_name is None or last_name is None:
                logger.error("Please provide either id or first name and last name")
                return 
            
            query = f"select id from home.labours where lower(first_name)= '{first_name.lower()}' and lower(last_name) = '{last_name.lower()}';"

            try:
                result = crud.read_from_mysql(query)
                id = result[0][0]

                logger.info(f"Id from labours table {result[0][0]}")

            except IndexError as err:
                 logger.error(f"Error Message: {str(err)} \n Please register yourself. No entry found.")
                 raise err
            except Exception as e:
                logger.error("Labour is not present. Please register first.")
                logger.error(f"Error Type: {type(e).__name__}")
                # logger.error(f"Error Message: {str(e)}")
                # raise e

            # except IndexError:
            #     logger.error(f"Error Message: {str(IndexError)}")

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_date = datetime.now().strftime('%Y-%m-%d')

        check_query = f"""
            SELECT id, start_time, end_time FROM attendance
            WHERE labour_id = {id} AND DATE(start_time)='{current_date}'
        """
        result = crud.read_from_mysql(check_query)
        logger.info(f"Data from labours table {result}")

        if len(result) == 0:
            insert_query = f"""
            INSERT INTO attendance (labour_id, start_time)
            VALUES ({id}, '{current_time}')
            """
            crud.inser_from_mysql(insert_query)
            logger.info(f"Labour {id} logged in at {current_time}")
        else:
            id = result[0][0]
            update_query = f"""
                UPDATE attendance
                SET end_time = '{current_time}'
                WHERE id = {id};
                """
            crud.inser_from_mysql(update_query)
            logger.info(f"Labour {id} logged out at {current_time}")

class Mistri(Labour):
    def  __init__(self, first_name, last_name, wage, role, skill, crud):
        super().__init__(first_name, last_name, wage, role, crud)
        self.skill = skill
        self.__save_to_skill_table()

    def __save_to_skill_table(self):
        insert_query = f"""INSERT INTO home.skills (labour_id, skills) 
                            VALUES  ({self.id}, '{self.skill}')"""
        
        self.crud.inser_from_mysql(insert_query)





# config = configparser.ConfigParser()
# config_filepath = (r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\PythonFundamentals\src_refactoring\resources\config_file.ini")
# config.read(config_filepath)
# decrypted_password = decrypt(config["mysql_database"]["password"])
# config.set("mysql_database","password", decrypted_password)

# mysql_db_conn_obj = MySqlConnection(config=config)
# mysql_db_conn_obj.connect()
# crud = MySqlCrudOperations(mysql_db_conn_obj.connection)

# my_obj5 = Labour("MyNm5", "Surname5", 5000, "Comp3", crud)
