__author__ = 'fei'

from db_model.model import Post
from db_model.model import get_session


def find_all_posts():
    return get_session().query(Post).all()


def find_post_by_post_id(post_id):
    return get_session().query(Post).filter_by(post_id=post_id).first()


def find_posts_by_category_id(category_id):
    return get_session().query(Post).filter_by(category_id=category_id).all()


def create_post(category_id, title, summary, content, user_id):
    get_session().add(Post(
        category_id=category_id, title=title, summary=summary, content=content, user_id=user_id))

    get_session().commit()


