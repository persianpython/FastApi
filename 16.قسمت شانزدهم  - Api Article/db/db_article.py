from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle


def create_article(db:Session, request:ArticleBase):
    article = DbArticle(title=request.title,
                        content=request.content,
                        published=request.published,
                        user_id=request.creator_id)
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(id, db:Session):
    return db.query(DbArticle).filter(DbArticle.id == id).first()
