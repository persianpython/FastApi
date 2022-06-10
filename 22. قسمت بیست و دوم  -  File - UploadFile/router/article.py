from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay, UserBase
from db import db_article
from db.database import get_db
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/article', tags=['article'])


# create article
@router.post('/', response_model=ArticleDisplay)
def create_article(article: ArticleBase, db=Depends(get_db)):
    return db_article.create_article(db, article)


# read article
@router.get('/{id}')
def get_article(id: int, db=Depends(get_db), current_user : UserBase= Depends(get_current_user)):
    return {
        "data": db_article.get_article(id, db),
        "current_user": current_user
    }

