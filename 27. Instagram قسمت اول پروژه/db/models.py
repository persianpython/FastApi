from db.database import Base
from sqlalchemy import Column, Integer, String


class UserBase(Base):
    __tablename__ = "user"

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
