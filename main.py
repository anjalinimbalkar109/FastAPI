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
@app.get("/users")
def get_users(name : str = None):
    return {
         "name" : name  
    }    

@app.get("/products")
def get_users(limit : int = 10 ):
    return {
        "limit" :  limit
    }

@app.get("/items")
def get_items(name : str = None, price : float = None):
    return{
        "name" : name,
        "price" : price
    }