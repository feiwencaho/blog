#encoding:utf8
'''
Created on 2015年10月4日
@author: fei
'''
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define, options
from handler.loginhandler import LoginHandler
from handler.homehandler import HomeHandler
from handler.categoryhandler import CategoryHandler
from handler.bloghandler import BlogHandler
from handler.basehandler import BaseHandler
define( 'port', default = 80, help = 'run on the given port', type = int )
class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/login',LoginHandler),
            (r'/',HomeHandler),
            (r'/category',CategoryHandler),
            (r'/blog',BlogHandler),
            (r'.*',BaseHandler)
        ]

        settings = {
            'static_path':os.path.join( os.path.dirname( __file__), 'static' ),
            'template_path':os.path.join(os.path.dirname(__file__), 'templates'),
            'cookie_secret':'LTUuWi7iImgJNDRdvAEB4beRGc/Qu=Wq=',
            'login_url':'/login',
            'debug':True,
            'auto_reload':True
            }
        tornado.web.Application.__init__(self, handlers = handlers,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer( Application(), xheaders=True )
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


