"""The Posts model file"""
from sqlalchemy import Column, ForeignKey, Integer, String

from database.db import Base


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=False)