from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
UPLOADS_DIR = os.path.join(BASE_DIR, "src", "uploads")
DATASETS_DIR = os.path.join(BASE_DIR, "src", "datasets")
def clear_directory(dir_path: str):
    if os.path.exists(dir_path):
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

@app.post("/upload/album")
async def upload_album(file: UploadFile = File(...)):
    albums_dir = os.path.join(UPLOADS_DIR, "album")
    os.makedirs(albums_dir, exist_ok=True)
    clear_directory(albums_dir)  # Clear old files before saving new one

    file_path = os.path.join(albums_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"Album cover '{file.filename}' uploaded successfully!", "filename": file.filename}


@app.post("/upload/audio")
async def upload_audio(file: UploadFile = File(...)):
    audio_dir = os.path.join(UPLOADS_DIR, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    clear_directory(audio_dir)  # Clear old files

    file_path = os.path.join(audio_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"Audio file '{file.filename}' uploaded successfully!", "filename": file.filename}


@app.post("/upload/dataset")
async def upload_dataset(file: UploadFile = File(...)):
    os.makedirs(DATASETS_DIR, exist_ok=True)
    clear_directory(DATASETS_DIR)  # Clear old files

    dataset_path = os.path.join(DATASETS_DIR, file.filename)
    with open(dataset_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"Dataset '{file.filename}' uploaded successfully!", "filename": file.filename}


@app.post("/upload/mapper")
async def upload_mapper(file: UploadFile = File(...)):
    os.makedirs(DATASETS_DIR, exist_ok=True)
    clear_directory(DATASETS_DIR)  # Clear old files

    mapper_path = os.path.join(DATASETS_DIR, file.filename)
    with open(mapper_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"Mapper '{file.filename}' uploaded successfully!", "filename": file.filename}