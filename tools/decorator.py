__author__ = 'fei'

from db_model.model import get_session


def db_flush(func):
    def wrapper(args):
        try:
            print 'before'
            results = func(args)
            get_session().commit()
            print 'after'
            return results
        except Exception as e:
            print e.message
            get_session().rollback()
            args.render('error.html')

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
