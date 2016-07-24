import tornado.ioloop
import tornado.web

from barcode.writer import ImageWriter
from barcode import pybarcode
import barcode

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # ean = barcode.get('ean', '123456', ImageWriter())
        # ean.save('test')
        # self.write('test.png')
        # self.set_header('Content-Type', 'application/octet-stream')
        # self.set_header('Content-Disposition', 'attachment; filename=test.txt')
        # with open('test.png', 'rb') as f:
        #     data = f.read()
        #     self.write(data)
        self.write('<img src="test.png">')


if __name__ == "__main__":
    # pass
    import os
    import time
    print time.strftime('%Y-%m-%d %H:%M:%S')
    # application = tornado.web.Application([
    #     (r"/", MainHandler),
    # ],
    #     static_path=os.path.join(os.path.dirname(__file__), 'test')
    # )
    # print os.path.join(os.path.dirname(__file__), 'test')
    # application.listen(8888)
    # tornado.ioloop.IOLoop.current().start()
    # ean = barcode.get('ean', '123456', ImageWriter())
    # ean.save('test')
    # for i in range(50):
    #     ean = barcode.get('ean', '0000000%s' % i, ImageWriter())
    #     ean.save('test/test%s' % i)