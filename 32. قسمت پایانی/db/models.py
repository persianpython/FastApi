from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    items = relationship("Post", back_populates='user')


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, index=True, primary_key=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates='items')
    comments = relationship("Comment", back_populates='post')


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, index=True, primary_key=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    timestamp = Column(DateTime)
    user = relationship("User")
    post = relationship("Post", back_populates='comments')
