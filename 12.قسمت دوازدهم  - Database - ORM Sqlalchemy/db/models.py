from db.database import Base
from sqlalchemy import Column, Integer, String


class DbUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
