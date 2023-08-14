from db.models import Comment
from schemas import CommentBase
from sqlalchemy.orm import Session
import datetime
from fastapi.exceptions import HTTPException
from fastapi import status


def create_comment(request: CommentBase, db: Session):
    new_comment = Comment(
        text=request.text,
        user_id=request.user_id,
        post_id=request.post_id,
        timestamp=datetime.datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_comments_by_post_id(id: int, db: Session):
    return db.query(Comment).filter(Comment.post_id == id).all()


def delete_comment(id: int, user_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if comment.user_id == user_id or comment.post.user.id == user_id:
        db.delete(comment)
        db.commit()
        return "OK"

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


