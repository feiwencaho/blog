__author__ = 'fei'

from db_model.model import Post
from db_model.model import get_session


def find_all_posts(start=None, stop=None):

    if start is not None and stop is not None:
        return get_session().query(Post).order_by(Post.create_time.desc()).slice(start, stop).all()
    else:
        return get_session().query(Post).order_by(Post.create_time.desc()).all()


def find_posts_count(category_id=None):
    conditions = dict()
    if category_id:
        conditions['category_id'] = category_id

    return get_session().query(Post).filter_by(**conditions).count()


def find_post_by_post_id(post_id):
    return get_session().query(Post).filter_by(post_id=post_id).first()


def find_posts_by_category_id(category_id):
    return get_session().query(Post).filter_by(category_id=category_id).order_by(Post.create_time.desc()).all()


def delete_post_by_post_id(post_id):
    get_session().delete(find_post_by_post_id(post_id))
    return

def create_post(category_id, title, summary, content, user_id):
    get_session().add(Post(
        category_id=category_id, title=title, summary=summary, content=content, user_id=user_id))
    get_session().flush()


