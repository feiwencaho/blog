# coding:utf8

__author__ = 'fei'


if __name__ == '__main__':
    s = u'阿斯顿'
    s1 = s.encode('utf8')
    print s1
    print s
    s2 = u'<p>\u5927\u8d5b\u7684</p>'
    s2 = s2.encode('utf8')
    print s2.decode('utf8')
