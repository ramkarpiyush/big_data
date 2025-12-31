from loguru import logger
from _src.main.databases.mysql_connector import *
from _src.main.utility.encrypt_decrypt import decrypt
from _src.main.factories.person_factory import PersonFactory
from _src.main.services.labour_service import LabourService
from _src.main.services.attendance_service import AttendanceService
from fastapi import FastAPI

import configparser
config = configparser.ConfigParser()

config_filepath = r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\PythonFundamentals\_src\resources\config_file.ini"
config.read(config_filepath)
config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

db = MySqlConnection.get_instance(config)
logger.info(f"Db connection {db}")

app = FastAPI()

@app.post("/createUser")
# Function to create a new labour dynamically
def create_user(first_name, last_name, wage, role):
    try:
        labour = PersonFactory.create_person("labour", first_name=first_name, last_name=last_name, wage=wage, role=role)
        logger.info(f"Value of labour object {labour}")
        labour_service = LabourService(db.connection)
        labour_id = labour_service.create_labour(labour)
        logger.info(labour_id)
        return {"status": "Success",
                "message": f"User created with ID {labour_id}"}
    except Exception as e:
        return {"status": "Fail",
                "Error": f"{str(e)}"}

@app.get("/getLabour/{labour_id}")
def get_using_labour_id(labour_id:int):
    labour_service = LabourService(db.connection)
    result = labour_service.get_labour(labour_id=labour_id)
    logger.info(f"Result Data Type: {type(result)}")
    return {"status": "Success", "Data": f"{result}"}

@app.get("/getLabour")
def get_using_labour_id():
    labour_service = LabourService(db.connection)
    result = labour_service.get_all_labour()
    return {"status": "Success", "Data": f"{result}"}

# Function to handle login/logout
def login_logout(labour_id=None, first_name=None, last_name=None):
    attendance_service = AttendanceService(db.connection)
    attendance_service.login_logout(labour_id, first_name, last_name)
    return "Attendance recorded successfully."

# result = create_user("User1", "kumar", 1500, "Electrician")
# logger.info(result)
# logger.info(f"Labour added with Id {result}")

# print(login_logout(first_name="manish", last_name="kumar"))

