#!/usr/bin/python
#-*- coding:utf8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define, options


define('port', default=8080, help='run on the given port', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test_upload.html')

    def post(self):
        print self.request.files['img']

        # 保存文件到本地
        # 得到文件的元数据
        file_matas = self.request.files['img']
        for file_meta in file_matas:
            with open('/home/fei/upload/' + file_meta['filename'], 'w') as f:
                f.write(file_meta['body'])

        self.redirect('/')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
        ]

        settings = {
            'template_path': '../templates',
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



