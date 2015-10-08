#encoding=utf8
'''
Created on 2015年10月5日
@author: fei
'''
from handler.basehandler import BaseHandler
from orm.models import User
from orm.orm import UserOrm

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')
        
    def post(self):
        userOrm = UserOrm(session=self.session)
        username = self.get_argument('username')
        password = self.get_argument('password')

        user = User(username=username,password=password)
        if userOrm.findUserByUser(user):
            #login success
            self.set_secure_cookie('username', username)
            self.write('1')
        else:
            #login fail
            self.write('0')
        
        
        
        
        