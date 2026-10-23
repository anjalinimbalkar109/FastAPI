from fastapi import FastAPI,HTTPException,Depends,Header
from jose import jwt
from datetime import datetime,timedelta,timezone

app = FastAPI()

SECRET_KEY ="mysecret"

ALGORITHM = "HS256"

# Create Token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return token

#Login API (Token Genration):
@app.post("/Login")
def login(username:str,password:str):
    if username !="admin" or password != "12345":
        raise HTTPException(status_code=401,detail="Invalid username or password")
    token = create_token({
         "sub":username
    })   
    return{
        "access_token" : token
    }   

#Token Verification:
def token_verify(token:str = Header(None)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,detail="Invalid or expired Token")

#Protected route
@app.get("/secure")
def secure_data(user = Depends(token_verify)):
    return{
        "message" : "Secured data accessed",
        "user" : user
    }        