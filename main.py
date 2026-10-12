from fastapi import FastAPI
from pydantic import BaseModel b  

app = FastAPI()

#Users page
@app.post("/create_user")
def create_user(user: dict):
    return{
        "message": "User created successfully",
        "user": user
    }