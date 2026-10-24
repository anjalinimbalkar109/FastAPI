from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = {
    "http://127.0.0.1:5173"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins= origin, #allowed FE
    allow_credentials=True,
    allow_methods=["*"], #GET,POST,PUT,DELETE
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {
        "message" : "CORS Enable API"
    }