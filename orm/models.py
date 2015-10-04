#coding=utf8
'''
Created on 2015年10月4日
@author: fei
'''
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column,String,Integer,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__='user'

    id=Column(String(32),primary_key=True)
    username=Column(String(32))
    password=Column(String(32))
    blogs=relationship('Blog')

class Category(Base):
    __tablename__='category'
    
    id=Column(String(32),primary_key=True)
    categoryname=Column(String(32))
    blogs=relationship('Blog')
    
class Blog(Base):
    __tablename__='blog'

    id=Column(String(32),primary_key=True)
    category_id=Column(String(32),ForeignKey='category.id')
    title=Column(String(64))
    summary=Column(String(256))
    content=Column(String())
    user_id=Column(String(32),ForeignKey='user.id')
    view_count=Column(Integer(8))
    create_time=Column(DateTime,default=datetime.now())
    
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session  = DBSession()
def getSession():
    return session



