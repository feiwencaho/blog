#! /usr/bin/python
# encoding:utf8
"""
Created on 2015年10月4日
@author: fei
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define, options
from handler.handler import LoginHandler, IndexHandler, EditHandler, TestHandler,\
    PostsHandler, CategoriesHandler, PostHandler, AboutHandler, LogoutHandler, BaseHandler, \
    AdminIndexHandler, InServiceHandler, PhotoHandler
from tools import session
import logging


define('port', default=8000, help='run on the given port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r'/(.*?)', InServiceHandler),
            (r'/', IndexHandler),
            (r'/login', LoginHandler),
            (r'/edit', EditHandler),
            (r'/posts', PostsHandler),
            (r'/categories', CategoriesHandler),
            (r'/post/([0-9]+)', PostHandler),
            (r'/photowall', PhotoHandler),
            (r'/about', AboutHandler),
            (r'/logout/([0-9]+)', LogoutHandler),
            (r'/admin/index', AdminIndexHandler),
            (r'/test', TestHandler),
            (r'/(.*?)', BaseHandler)
        ]

        settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'cookie_secret': 'LTUuWi7iImgJNDRdvAEB4beRGc/Qu=Wq=',
            'login_url': '/login',
            # 'debug': True,
            # 'auto_reload': True,

            # redis settings
            'session_secret': 'session_secret',
            'store_options': {
                'redis_host': 'localhost',
                'redis_port': 6379,
                'redis_pass': '123456',
            },
            'session_timeout': 60*60*24,

            'upload_path': '/var/www/feiwenchao/upload/post'
        }
        tornado.web.Application.__init__(self, handlers=handlers, **settings)
        self.session_manager = session.SessionManager(
            settings['session_secret'], settings['store_options'], settings['session_timeout'])


def log():
    logging.basicConfig(
        filename='/var/log/blog.log',
        filemode='a',
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        level=logging.INFO
    )


if __name__ == '__main__':
    log()
    try:

        tornado.options.parse_command_line()
        for i in options.items():
            print i

        http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        logging.error(e)
