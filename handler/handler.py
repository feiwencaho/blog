#encoding=utf8
'''
Created on 2015年10月5日
@author: fei
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from db_model.model import User
import db_table.user
import db_table.category
import db_table.post
from basehandler import BaseHandler
from tools.decorator import db_flush
from tornado.web import authenticated


class LoginHandler(BaseHandler):

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        # user = User(username=username, password=password)
        u = db_table.user.find_user_by_username(username)
        if u:
            if u.password == password:
                #login success
                # self.set_secure_cookie('username', username)
                self.session['username'] = username
                self.session.save()
                print 'session ================= ', self.session['username']
                self.write('1')
        else:
            #login fail
            self.write('0')


class IndexHandler(BaseHandler):
    @db_flush
    def get(self):
        username = self.get_current_user()
        user = None
        if username:
            user = db_table.user.find_user_by_username(username)
        current_page = 0
        start = self.get_argument('start', None)
        stop = None
        limit = self.get_argument('limit', None)
        if start is not None and limit is not None:
            stop = int(start) + int(limit)
            current_page = int(start) / 5
        posts = db_table.post.find_all_posts(start=int(start) if start else None, stop=stop)
        total = db_table.post.find_posts_count()

        categories = db_table.category.find_all_categories()
        return self.render('index.html',
                           posts=posts, categories=categories, user=user, total=total, current_page=current_page)


class EditHandler(BaseHandler):
    # @authenticated
    def get(self):
        username = self.get_current_user()
        user = None
        if username:
            user = db_table.user.find_user_by_username(username)
        categories = db_table.category.find_all_categories()
        return self.render('write.html', categories=categories, user=user)


class CategoriesHandler(BaseHandler):
    def get(self):
        pass

    @db_flush
    # @authenticated
    def post(self):
        categoryname = self.get_argument('categoryname', None)
        if categoryname:
            db_table.category.create_category(categoryname=categoryname)
        else:
            raise Exception('categoryname cannot be empty!')

    # @authenticated
    def delete(self, category_id):
        return db_table.category.delete_category_by_id(category_id)


class PostsHandler(BaseHandler):
    def get(self):
        user = None
        username = self.get_current_user()
        start = self.get_argument('start', 0)
        limit = self.get_argument('limit', 5)
        # total = 10
        if username:
            user = db_table.user.find_user_by_username(username)
        category_id = self.get_argument('category_id', None)
        if category_id:
            categories = db_table.category.find_all_categories()
            posts = db_table.post.find_posts_by_category_id(category_id)
            total = db_table.post.find_posts_count(category_id=category_id)
            current_page = 0
            start = self.get_argument('start', None)
            limit = self.get_argument('limit', None)
            if start is not None and limit is not None:
                current_page = int(start) / 5

            datas = dict(
                posts=posts,
                categories=categories,
                user=user,
                total=total,
                current_page=current_page
            )
            return self.render('index.html', **datas)

    @db_flush
    # @authenticated
    def post(self):
        title = self.get_argument('title', None)
        content = self.get_argument('body', None)
        print 'title ========= ', title.encode('utf8')
        print 'content ========== ', content.encode('utf8')
        summary = self.get_argument('summary', None)
        user = db_table.user.find_user_by_username(self.get_current_user())
        category_id = self.get_argument('category_id', None)
        # db_table.category.create_category(categoryname=categoryname)
        if db_table.category.find_category_by_id(category_id):
            db_table.post.create_post(
                category_id=category_id,
                title=title,
                summary=summary,
                content=content,
                user_id=user.user_id if user else 1)

            return self.redirect('/edit')
        else:
            raise Exception('category is not existed!')


class PostHandler(BaseHandler):
    def get(self, post_id):
        user = None
        username = self.get_current_user()
        if username:
            user = db_table.user.find_user_by_username(username)
        post = db_table.post.find_post_by_post_id(post_id)
        return self.render('post.html', post=post, user=user)

    # @authenticated
    @db_flush
    def delete(self, post_id):
        1/0
        db_table.post.delete_post_by_post_id(post_id)

        posts = db_table.post.find_all_posts()
        # return self.render('admin_index.html', posts=posts)
        # return self.redirect('/admin/index')
        return self.write(str(post_id))


class AboutHandler(BaseHandler):
    def get(self):
        user = None
        username = self.get_current_user()
        if username:
            user = db_table.user.find_user_by_username(username)
        self.render('about.html', user=user)


class LogoutHandler(BaseHandler):
    def get(self, user_id):
        self.session['username'] = None
        self.session.save()
        self.redirect('/')


class SearchHandler(BaseHandler):
    def get(self):
        pass


class AdminIndexHandler(BaseHandler):
    def get(self):
        posts = db_table.post.find_all_posts()

        return self.render('admin_index.html', posts=posts)


