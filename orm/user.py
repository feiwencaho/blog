#coding=utf8

'''
Created on 2015年10月4日
@author: fei
'''
from orm.models import Category, User, Blog

class UserOrm():
    def __init__(self, session):
        self.session = session
        
    def findUserById(self, user_id):
        return self.session.query(User).filter_by(id=user_id).one()
    
    def findUserByUser(self, user):
        return self.session.query(User).filter_by(username=user.username,password=user.password).first()
    
class CategoryOrm():
    def __init__(self, session):
        self.session = session
        
    def findAllCategories(self):
        return self.session.query(Category).all()

    def addCategory(self, Category):
        self.session.add(Category)

class BlogOrm():
    def __init__(self, session):
        self.session = session

    def findBlogsByUser(self, user_id):
        return self.session.query(Blog).filter(user_id=user_id).all()
    
    def addBlog(self, Blog):
        self.session.add(Blog)
    
        
        