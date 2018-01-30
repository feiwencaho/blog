__author__ = 'fei'


from db_model.model import Praise
from db_model.model import get_session
from datetime import datetime
from sqlalchemy.sql import exists


def create_praise(ip):
    now = datetime.now()
    return get_session().add(Praise(ip=ip, create_time=now))


def find_praise_count():
    return get_session().query(Praise).count()


def is_existed(ip):
    return get_session().query(exists().where(Praise.ip == ip)).scalar()


def find_praise(ip):
    return get_session().query(Praise).filter_by(ip=ip).first()


