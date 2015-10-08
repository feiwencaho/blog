#coding=utf8
'''
@author: fei
'''

from handler.basehandler import BaseHandler
from orm.orm import CategoryOrm

# 处理和分类有关的请求
class CategoryHandler(BaseHandler):
    #在初始化方法中传入category的orm
    def initialize(self):
        BaseHandler.initialize(self)
        self.categoryOrm = CategoryOrm(session=self.session)

    def get(self):
        categories = self.categoryOrm.findAllCategories()
        self.render('category.html',categories=categories)

    def post(self):
        pass
    
class AddCategoryHandler(BaseHandler):
    def __init__(self):
        self.categoryOrm = CategoryOrm(session=self.session)

    def get(self):
        pass

    def post(self):
        pass

class EditCategoryHandler(BaseHandler):
    def __init__(self):
        self.categoryOrm = CategoryOrm(session=self.session)

    def get(self):
        pass

    def post(self):
        pass

class DeleteCategoryHandler(BaseHandler):
    def __init__(self):
        self.categoryOrm = CategoryOrm(session=self.session)

    def get(self):
        pass
    
    def post(self):
        pass

