from db_model.model import User, get_session


def create_user(user):
    return get_session().add(user)


def find_user_by_id(user_id):
    return get_session().query(User).filter_by(user_id=user_id).one()


def update_user(user):
    u = get_session().query(User).filter_by(username=user.username).one()
    if u:
        u.password = user.password


def find_user_by_username(username):
    return get_session().query(User).filter_by(username=username).first()


def find_all_users():
    return get_session().query(User).all()

if __name__ == '__main__':
    # user = find_user_by_id(1)
    # print user.username
    # user = User(username='zhangsan1', password='123')
    # create_user(user)
    # get_session().commit()
    # users = find_all_users()
    # print users
    user = find_user_by_username('admin')
    print user.password
    user.password = '0000'
    get_session().commit()
    # update_user()
    print find_user_by_username('admin').password











