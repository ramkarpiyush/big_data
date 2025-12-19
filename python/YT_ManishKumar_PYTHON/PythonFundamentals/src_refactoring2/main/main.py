from loguru import logger
from src_refactoring2.main.databases.mysql_connector import *
from src_refactoring2.main.utility.encrypt_decrypt import decrypt
from src_refactoring2.main.factories.person_factory import PersonFactory
from src_refactoring2.main.services.labour_service import LabourService
from src_refactoring2.main.services.attendance_service import AttendanceService

import configparser
config = configparser.ConfigParser()

config_filepath = r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\PythonFundamentals\src_refactoring2\resources\config_file.ini"
config.read(config_filepath)
config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

db = MySqlConnection.get_instance(config)
logger.info(f"Db connection {db}")

# Function to create a new labour dynamically
def create_user(first_name, last_name, wage, role):
    labour = PersonFactory.create_person("labour", first_name=first_name, last_name=last_name, wage=wage, role=role)
    logger.info(f"Value of labour object {labour}")
    labour_service = LabourService(db.connection)
    labour_id = labour_service.create_labour(labour)
    logger.info(labour_id)
    return labour_id

# Function to handle login/logout
def login_logout(labour_id=None, first_name=None, last_name=None):
    attendance_service = AttendanceService(db.connection)
    attendance_service.login_logout(labour_id, first_name, last_name)
    return "Attendance recorded successfully."

result = create_user("User1", "kumar", 1500, "Electrician")
logger.info(result)
logger.info(f"Labour added with Id {result}")

# print(login_logout(first_name="manish", last_name="kumar"))

