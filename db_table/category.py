__author__ = 'fei'


from db_model.model import Category
from db_model.model import get_session


def create_category(categoryname):
    return get_session().add(Category(categoryname=categoryname))


def find_all_categories():
    return get_session().query(Category).all()


def find_category_by_id(category_id):
    return get_session().query(Category).filter_by(category_id=category_id).one()


def create_category(categoryname):
    return get_session().add(Category(categoryname=categoryname))



def delete_category_by_id(category_id):
    return get_session().query(Category).delete()


def update_category(category):
    pass
