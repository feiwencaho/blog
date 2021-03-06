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
import db_table.praise
from basehandler import BaseHandler
from tools.decorator import db_flush
from tornado.web import authenticated
import os
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
import json
import uuid
import time
import logging

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


class InServiceHandler(BaseHandler):
    def get(self, *args):
        self.render('in_service.html')


class TestHandler(BaseHandler):
    def get(self):
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'upload/post/test.md'), 'r') as f:
            content = f.read()
            renderer = HighlightRenderer()
            markdown = mistune.Markdown(renderer=renderer)
            result = markdown(content)
            self.write(result)


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', error='')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        # user = User(username=username, password=password)
        u = db_table.user.find_user_by_username(username)
        if u:
            if u.password == password:
                # login success
                # self.set_secure_cookie('username', username)
                self.session['username'] = username
                self.session.save()
                # self.write('1')
                self.redirect('/admin/index')
        else:
            #login fail
            self.render('login.html', error='用户名或密码错误')


class IndexHandler(BaseHandler):
    @db_flush
    def get(self):
        username = self.get_current_user()
        user = None
        if username:
            user = db_table.user.find_user_by_username(username)
        current_page = 0
        start = int(self.get_argument('start', 0))
        stop = None
        limit = int(self.get_argument('limit', 5))

        if start < 0:
            start = 0
        if limit < 0:
            limit = 5
        if start is not None and limit is not None:
            stop = int(start) + int(limit)
            current_page = int(start) / 5
        posts = db_table.post.find_all_posts(start=start, stop=stop)
        total = db_table.post.find_posts_count()

        categories = db_table.category.find_all_categories()
        return self.render('index.html',
                           posts=posts,
                           categories=categories,
                           user=user,
                           total=total,
                           current_page=current_page,
                           category_id=-1)


class EditHandler(BaseHandler):
    @authenticated
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
    @authenticated
    def post(self):
        categoryname = self.get_argument('categoryname', None)
        if categoryname:
            db_table.category.create_category(categoryname=categoryname)
            return self.redirect('/admin/index')
        else:
            raise Exception('categoryname cannot be empty!')

    @authenticated
    def delete(self, category_id):
        return db_table.category.delete_category_by_id(category_id)


class PostsHandler(BaseHandler):
    def get(self):
        user = None
        username = self.get_current_user()
        start = int(self.get_argument('start', 0))
        limit = int(self.get_argument('limit', 5))
        if start < 0:
            start = 0

        if limit < 0:
            limit = 5

        # total = 10
        if username:
            user = db_table.user.find_user_by_username(username)
        category_id = int(self.get_argument('category_id', -1))
        if category_id:
            categories = db_table.category.find_all_categories()
            total = db_table.post.find_posts_count(category_id=category_id if category_id != -1 else None)
            current_page = 0
            if start is not None and limit is not None:
                current_page = int(start) / 5
            if category_id == -1:
                posts = db_table.post.find_all_posts(start=start, stop=start + limit)
            else:
                posts = db_table.post.find_posts_by_category_id(category_id, start=start, stop=start+limit)
            datas = dict(
                posts=posts,
                categories=categories,
                user=user,
                total=total,
                current_page=current_page,
                category_id=category_id
            )
            return self.render('index.html', **datas)

    @db_flush
    @authenticated
    def post(self):
        format_date = time.strftime('%Y%m%d')
        upload_path = os.path.join(self.settings['upload_path'], format_date)
        # 提取表单中‘name’为‘file’的文件元数据
        file_metas = self.request.files['post']
        # 创建博文文件夹,格式为年月日
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        category_id = self.get_argument('category_id', None)
        for meta in file_metas:
            filename = meta['filename']
            if filename.endswith('.md') or filename.endswith('.markdown') or filename.endswith('.mkd'):
                filename = '%s-%s' % (filename, str(uuid.uuid1()).upper())
                filepath=os.path.join(upload_path, filename)
                with open(filepath, 'w') as up:
                    up.write(meta['body'])
                title = self.get_argument('title', None)
                summary = self.get_argument('summary', None)
                db_table.post.create_post(
                    category_id=category_id,
                    title=title,
                    summary=summary,
                    path=filepath,
                    create_time=1,
                    user_id=1)
            else:
                raise Exception('must be markdown file!')
        self.redirect('/admin/index')


class PostHandler(BaseHandler):
    def get(self, post_id):
        user = None
        username = self.get_current_user()
        if username:
            user = db_table.user.find_user_by_username(username)
        post = db_table.post.find_post_by_post_id(post_id)
        content = ''
        with open(post.path, 'r') as f:
            while 1:
                data = f.read(1024 * 10)
                if data:
                    content += data
                else:
                    break
        renderer = HighlightRenderer()

        markdown = mistune.Markdown(renderer=renderer)

        content = markdown(content)
        return self.render('post.html', post=post, user=user, content=content)

    @authenticated
    @db_flush
    def delete(self, post_id):
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


class PhotoHandler(BaseHandler):
    def get(self):
        self.render('photo_wall.html')



class AdminIndexHandler(BaseHandler):
    @authenticated
    def get(self):
        posts = db_table.post.find_all_posts()
        categorys = db_table.category.find_all_categories()
        return self.render('admin_index.html', posts=posts, categorys=categorys)


class PraiseHandler(BaseHandler):
    @db_flush
    def post(self):
        ip = self.request.remote_ip
        if not db_table.praise.is_existed(ip):
            db_table.praise.create_praise(ip)

    def get(self):
        return self.write(dict(total=522 + db_table.praise.find_praise_count()))


class CheckPraiseHandler(BaseHandler):
    def get(self):
        is_existed = db_table.praise.is_existed(self.request.remote_ip)
        return self.write(dict(is_existed=is_existed))

