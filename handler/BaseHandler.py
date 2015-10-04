'''
Created on 2015年10月4日

@author: fei
'''
import tornado

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user', '')

    def initialize(self):
        pass
        
    def get(self, *args, **kwargs):
        self.render('404.html')
        
    def on_finish(self):
        self.session.close()
        
        
        
        
        