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
from handler.handler import LoginHandler, IndexHandler, EditHandler, \
    PostsHandler, CategoriesHandler, PostHandler, AboutHandler


define('port', default=8080, help='run on the given port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/login', LoginHandler),
            (r'/edit', EditHandler),
            (r'/posts', PostsHandler),
            (r'/categories', CategoriesHandler),
            (r'/post/([0-9]?)', PostHandler),
            (r'/about', AboutHandler)
        ]

        settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'cookie_secret': 'LTUuWi7iImgJNDRdvAEB4beRGc/Qu=Wq=',
            'login_url': '/',
            'debug': True,
            'auto_reload': True
        }
        tornado.web.Application.__init__(self, handlers=handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

