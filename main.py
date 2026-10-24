from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.responses import FileResponse
import os
import shutil
from pathlib import Path

app = FastAPI()

#step 1 : Ensure upload folder exist

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#Step 3: Upload file API
@app.post("/upload")
def upload_file(file: UploadFile =File(...)):
    filename= file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)

    if not filename:
        raise HTTPException(
            status_code=400,
            detail="File not selected"
        )

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

        return {
            "message" : "File Uploaded succesfully",
            "fileName" : filename,
            "file_url" : f"http://127.0.0.1:8000/files/{filename}"
        }

#Step 4 : Get URL API

@app.get("/files/{filename}")
def get_file(filename:str):
    upload_dir = Path(UPLOAD_DIR).resolve()
    file_path = (upload_dir / filename).resolve()

    if file_path.parent != upload_dir or not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return FileResponse(file_path)

@app.get("/")
def home():
    return {
        "message" : "File uploded API running"
    } 