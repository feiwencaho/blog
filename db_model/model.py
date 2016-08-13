#coding=utf8
'''
Created on 2015年10月4日
@author: fei
'''
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column,String,Integer,DateTime,create_engine,BLOB
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(32))
    password = Column(String(32))
    posts = relationship('Post', backref='user')

    def __repr__(self):
        return '<User %s>' % self.username


class Category(Base):
    __tablename__ = 'category'
    
    category_id = Column(Integer, autoincrement=True, primary_key=True)
    categoryname = Column(String(32))
    posts = relationship('Post', backref='category')


class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer,autoincrement=True, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.category_id'))
    title = Column(String(64))
    summary = Column(String(1024))
    path = Column(String(1024))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    view_count = Column(Integer, default=0)
    create_time = Column(DateTime, default=datetime.now())


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/blog', echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_session():
    return session


def rebuild_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    rebuild_db()
