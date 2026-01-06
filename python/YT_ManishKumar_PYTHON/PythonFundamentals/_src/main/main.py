from loguru import logger
from _src.main.databases.mysql_connector import MySqlConnection, MySqlCrudOperations
from _src.main.utility.encrypt_decrypt import decrypt
from _src.main.factories.person_factory import PersonFactory
from _src.main.services.labour_service import LabourService
from _src.main.services.attendance_service import AttendanceService
from _src.main.models.all_models import User, UIResponse, Attendance
from fastapi import FastAPI, HTTPException

import configparser
config = configparser.ConfigParser()

config_filepath = r"D:\GitLocal\big_data\python\YT_ManishKumar_PYTHON\PythonFundamentals\_src\resources\config_file.ini"
config.read(config_filepath)
config.set("mysql_database","password", decrypt(config["mysql_database"]["password"]))

db = MySqlConnection.get_instance(config)
logger.info(f"Db connection {db}")

app = FastAPI(title="API to buid Home", description= "All this set of API can help u to build  and predict the cost for your house")

@app.post("/createUser", tags=["User"])
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
    
@app.post("/createMistri", tags= ["user"])
def create_user(user: User):
    try:
        user = user.model_dump()
        logger.info(f"Value of user is {user}")
        labour = PersonFactory.create_person("Mistri", first_name=user['first_name'], last_name=user['last_name'], wage=user['wage'], role=user['role'])
        logger.info(f"Value of labour object {labour}")
        labour_service = LabourService(db.connection)
        labour_id = labour_service.create_labour(labour)
        logger.info(labour_id)
        return UIResponse(status= "Success", status_code=200, data= user, message= f"User created with ID {labour_id}")
    except Exception as e:
        # raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
        return UIResponse(status= "Failed", status_code=400, data= user, message= f"Error: {str(e)}")

@app.get("/getLabour/{labour_id}", tags=["Labour"])
def get_using_labour_id(labour_id:int):
    labour_service = LabourService(db.connection)
    result = labour_service.get_labour(labour_id=labour_id)
    logger.info(f"Result Data Type: {type(result)}")
    return {"status": "Success", "Data": f"{result}"}


@app.get("/getLabour", tags=["Labour"])
def get_using_labour_id():
    labour_service = LabourService(db.connection)
    result = labour_service.get_all_labour()
    return {"status": "Success", "Data": f"{result}"}

# Function to handle login/logout
@app.post("/attendance", tags=["labour"])
def login_logout(attendance: Attendance):
    attendance = attendance.model_dump()
    attendance_service = AttendanceService(db.connection)
    attendance_service.login_logout(attendance["labour_id"], attendance["first_name"], attendance["last_name"])
    # return "Attendance recorded successfully."
    return UIResponse(status= "Success", status_code=200, data= attendance, message= "Attendance recorded successfully.")







# result = create_user("User1", "kumar", 1500, "Electrician")
# logger.info(result)
# logger.info(f"Labour added with Id {result}")

# print(login_logout(first_name="manish", last_name="kumar"))

