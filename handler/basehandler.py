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
        return self.session.get('username')

    def get(self, arg):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        print 'write_error is called...'
        print 'status_code :', status_code
        if status_code == 404:
            self.render('404.html')
        print 'exc_info :', kwargs.get('exc_info', None)
        # if status_code == 500:
        #     self.render('error.html')
    # def finish(self, chunk=None):
    #     get_session().commit()
    #     print 'finish ......... '
