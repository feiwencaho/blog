#encoding=utf8
'''
Created on 2015年10月4日
@author: fei
'''
import tornado.web
from db_model.model import get_session
from tools import session


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.session = session.Session(self.application.session_manager, self)
        self.db_session = get_session()

    def get_current_user(self):
        print 'username :::::::: ', self.session.get('username')
        return self.session.get('username')
        # return '123'
    # def get_current_user(self):
    #     return self.get_secure_cookie('username')
    # def initialize(self):
    #     self.db_session = get_session()

    def get(self):
        self.write_error(404)

    # def on_finish(self):
    #     print('get_current_user is called...')
    #     return self.get_secure_cookie('username')

    def write_error(self, status_code, **kwargs):
        print('write_error is called...')
        if status_code == 404:
            self.render('404.html')

        if status_code == 500:
            self.render('error.html')