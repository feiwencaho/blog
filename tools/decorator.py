__author__ = 'fei'

from db_model.model import get_session
import logging

def db_flush(func):
    def wrapper(*args, **kwargs):
        try:
            results = func(*args, **kwargs)
            return results
        except Exception as e:
            logging.error(e)
            get_session().rollback()
            args[0].render('error.html')
            raise
        finally:
            get_session().commit()
    return wrapper


def b(func):
    def wrapper(args):
        print 'before'
        s = func(args)
        print 'after'
        return s
    return wrapper


@b
def a(text):
    print text
    return text


if __name__ == "__main__":
    print a('asd')
