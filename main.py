from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

    
#Users page
@app.post("/create_user")
def create_user(user : User):
    return{
        "message": "User created successfully",
        "user": user
    }