from fastapi import FastAPI,status, HTTPException


app = FastAPI()

@app.post("/create_user", status_code = status.HTTP_201_CREATED)
def create_user():
    return{
        "message" : "User created"
    }

@app.get("/user", status_code = status.HTTP_200_OK)
def get_user():
    return {
        "status" : "Success",
        "message" : "User fetched successfully",
        "data" : {
            "name" : "John Doe",
            "age" : 21
        }
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail = "User not found"
        )
    return {
        "id" : 1,
        "name" : "John Doe",
    }