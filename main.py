#Dyanamic route - Path parameters
from fastapi import FastAPI

app = FastAPI()

#users route 
@app.get("/users/{user_id}")
def get_user(user_id : int):
    return {
          "user_id": user_id
    }