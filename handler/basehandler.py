#encoding=utf8
'''
Created on 2015年10月4日
@author: fei
'''
import tornado.web
from db_model.model import get_session


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username')

    def initialize(self):
        self.session = get_session()

    def get(self):
        self.write_error(404)

    def on_finish(self):
        print('get_current_user is called...')
        return self.get_secure_cookie('username')

    def initialize(self):
        print('initialize is called...')
        self.session = get_session()

    def get(self):
        print('get is called...')
        self.write_error(404)

    def on_finish(self):
        print('on_finish is called...')
        self.session.close()

    def write_error(self, status_code, **kwargs):
        print('write_error is called...')
        if status_code == 404:
            self.render('404.html')

        if status_code == 500:
            self.write('xixi500')