import random
import shutil
from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from db.database import get_db
from db import db_post
from string import ascii_letters
from typing import List
from schemas import PostDisplay, PostBase

router = APIRouter(prefix="/post", tags=['post'])

image_url_tyopes = ["url", "uploaded"]


@router.post('/create_post', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_tyopes:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="image url type should be 'url' or 'uploaded'")
    return db_post.create_post(request, db)


@router.get("/", response_model=List[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)


@router.post("/upload_file")
def upload_file(file: UploadFile = File(...)):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit('.', 1))
    path_file = f"uploaded_files/{new_name}"
    with open(path_file, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"path_file": path_file}
