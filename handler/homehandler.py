#encoding=utf8
'''
Created on 2015年10月5日
@author: fei
'''
from handler.basehandler import BaseHandler
import tornado.web

class HomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html')
        
        
        