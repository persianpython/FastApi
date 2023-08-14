from db.models import User
from schemas import UserBase
from sqlalchemy.orm import Session
from db.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status


def create_user(request: UserBase, db: Session):
    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(username:str, db:Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User Not Found !")

    return user
