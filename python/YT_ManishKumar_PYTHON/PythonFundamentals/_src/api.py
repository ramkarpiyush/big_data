from fastapi import FastAPI

app = FastAPI()
    
@app.get("/getUsers")
def get_user():
    return {"user1": "Manish"}

@app.post("/postUserDataToTable")
def create_user(name:str, gender:str, email:str, city:str):
    return {"Message": "User added successfully"}

