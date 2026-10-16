from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect("test.db" , check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMERY KEY,
        title TEXT,
        completed TEXT
    )
""")

conn.commit()

@app.get("/")
def home():
    return {
        "message" : "SQLite Connected fine"
    }




