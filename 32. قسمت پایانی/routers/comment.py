from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from db.database import get_db
from db import db_comment
from typing import List
from schemas import CommentDisplay, CommentBase, UserAuth
from auth import oauth2

router = APIRouter(prefix="/comment", tags=['comment'])


@router.post('/create_comment', response_model=CommentDisplay)
def create_post(request: CommentBase, db: Session = Depends(get_db),
                current_user:UserAuth = Depends(oauth2.get_current_user)):
    return db_comment.create_comment(request, db)


@router.post('/delete/{id}')
def delete_comment(id: int, db: Session = Depends(get_db),
                current_user:UserAuth = Depends(oauth2.get_current_user)):
    return db_comment.delete_comment(id=id, db=db, user_id=current_user.id)


@router.get("/{id}", response_model=List[CommentDisplay])
def get_comments(id:int, db: Session = Depends(get_db)):
    return db_comment.get_comments_by_post_id(id=id, db=db)

