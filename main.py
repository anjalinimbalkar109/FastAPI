# Dependency Example with Autherization

from fastapi import FastAPI, Depends,Header,HTTPException

app = FastAPI()

def verify_token(token: str = Header(None)):
    if token != "MysecretToken":
        raise HTTPException(
            status_code=401,
            detail = "Unautharized"
        )
    return{
        "user" : "Autherized user"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return{
        "message" : "Secure data accessed",
        "user" : user
    }

# Dependancy Simple Example:

# from fastapi import FastAPI, Depends

# def get_current_user():
#     return{
#        "User" : "Jay"
#     }

# @app.get("/profile")
# def read_profile(user = Depends(get_current_user)):
#     return user

# @app.get("/dashboard")
# def dashboard(user = Depends(get_current_user)):
#     return user