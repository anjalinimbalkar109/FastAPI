from fastapi import FastAPI

app = FastAPI()

#  Home route
# @app.get("/")
# def home():
#     return {"message": "Welcome to the FastAPI application! venv"}

# About route
# @app.get("/about")
# def about():
#     return {"message": "This is aboutpage"}

#Users page
@app.get("/users/{user_id}")
def users(user_id: int):
    return {
        "User ID" : user_id
    }    