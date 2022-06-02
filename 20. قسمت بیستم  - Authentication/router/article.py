from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from db import db_article
from db.database import get_db
from auth.oauth2 import oauth2_scheme

router = APIRouter(prefix='/article', tags=['article'])


# create article
@router.post('/', response_model=ArticleDisplay)
def create_article(article: ArticleBase, db=Depends(get_db)):
    return db_article.create_article(db, article)


# read article
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db=Depends(get_db), token:str=Depends(oauth2_scheme)):
    return db_article.get_article(id, db)

