"""The Posts model file"""
from database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable==False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=False)