from loguru import logger
from src_refactoring.main.databases.mysql_connector import MySqlConnection, MySqlCrudOperations
from src_refactoring.main.main import *

class Labour:
    # total_cnt = 0
    def __init__(self, first_name, last_name, wage, role, crud):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage
        self.role = role
        self.crud = crud
        self.check_for_email(crud)
        self.__save_to_database(self.crud)
        # self.check_for_email(crud)
        # Labour.total_cnt += 1

    def __save_to_database(self, crud):
        query = f"select id from home.labours where lower(first_name) = '{self.first_name}' and lower(last_name) = '{self.last_name}';"
        # logger.info(f"Crud: {crud}")
        result = crud.read_from_mysql(query)

        if result:
            logger.info(f"Labout already exists with ID: {result[0][0]}")
            return result[0][0]
        
        email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"

        insert_query = f"""
            INSERT INTO labours (first_name, last_name, wage, role, email)
            values ('{self.first_name}', '{self.last_name}', {self.wage}, '{self.role}', '{email}')
        """
        # logger.info(f"INSERT QUERY: {insert_query}")

        crud.inser_from_mysql(insert_query)

        result = crud.read_from_mysql(query)
        logger.info(f"New labour added with ID: {result[0][0]}")
        return result[0][0]

    def check_for_email(self, crud):
        email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"
        count_sql = f"SELECT COUNT(*) AS cnt FROM home.labours WHERE email = '{email}'"
        # logger.info(count_sql)
        rows = crud.read_from_mysql(count_sql)
        logger.info(rows[0][0])
        # count = rows[0]["cnt"] if rows else 0   
        return rows     


    def login(self):
        pass



