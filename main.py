                                         # Query Branch

from fastapi import FastAPI

app = FastAPI()

# # Home route
# @app.get("/")
# def home():
#     return {"message": "Welcome to the FastAPI application! venv"}

# #About route
# @app.get("/about")
# def about():
#     return {"message": "This is aboutpage"}

#Users page
@app.get("/users/{name}")
def users(name : str):
    return {
         "name" : name  
    }    
