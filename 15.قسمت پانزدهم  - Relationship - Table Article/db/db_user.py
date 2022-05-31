from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
    user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db:Session):
    return db.query(DbUser).all()


def get_user(id, db:Session):
    return db.query(DbUser).filter(DbUser.id == id).first()


def delete_user(id, db:Session):
    user = get_user(id, db)
    db.delete(user)
    db.commit()
    return 'ok'


def update_user(id, db:Session, request:UserBase):
    user = db.query(DbUser).filter(DbUser.id==id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password),
    })
    db.commit()
    return 'ok'