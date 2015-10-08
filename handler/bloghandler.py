# coding=utf8
'''
Created on 2015年10月5日

@author: fei
'''
from handler.basehandler import BaseHandler

class BlogHandler(BaseHandler):
        
    def get(self):
        self.render('blog.html')
        
class AddBlogHandler(BaseHandler):
    def get(self):
        pass
    
    def post(self):
        pass

class EditBlogHandler(BaseHandler):
    def get(self):
        pass
    
    def post(self):
        pass

class DeleteBlogHandler(BaseHandler):
    def get(self):
        pass
    
    def post(self):
        pass
    
    
    



        
    
