#-*- coding:utf8 -*-

__author__ = 'fei'


# def deco(arg):
#     def _deco(func):
#         def __deco(*args, **kwargs):
#             print 'before called...deco_arg:%s' % arg
#             res = func(*args, **kwargs)
#             print 'after called...deco_arg:%s' % arg
#             return res
#         return __deco
#     return _deco
#
#
# @deco('aa')
# def test(a, b):
#     print 'running...'
#     return a + b
#
#
# @deco('aa')
# def test1(a, b, c):
#     print 'test1 is running...'
#     return a + b + c


##################################################################
# 让装饰器带类参数
# class lock(object):
#     @staticmethod
#     def acquire():
#         print 'acquire is running...'
#
#     @staticmethod
#     def release():
#         print 'release is running...'
#
#
# def deco1(cls):
#     def _deco(func):
#         def __deco(*args, **kwargs):
#             print 'before func called...'
#             cls.acquire()
#             cls.release()
#             res = func(*args, **kwargs)
#             print 'after func called...'
#             return res
#         return __deco
#     return _deco


# @deco1(lock)
# def test2(a, b):
#     print 'test2 is running...'
#     return a + b


if __name__ == '__main__':
    # print test(1, 2)
    # print test1(1, 2, 3)
    # print test2(3, 5)
    print('ad','ddd')