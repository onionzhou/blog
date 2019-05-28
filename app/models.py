#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 9:03 AM
# @Author  : onion
# @Site    : 
# @File    : models.py
# @Software: PyCharm


from  werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as TJWSS
from flask import current_app
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))

    confirmed =db.Column(db.Boolean,default=False) #邮件确认生效标志

    essays = db.relationship('Essay', backref='author', lazy='dynamic')


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_annoyous(self):
        return False

    def get_id(self):
        try:
            return self.id  # 返回unicode
        except NameError:
            return str(self.id)

    def gen_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def gen_confirm_token(self,exp=3600):
        t =TJWSS(current_app.config['SECRET_KEY'],exp)
        #加密
        return t.dumps({'id':self.id})

    def confirm(self,token):
        t = TJWSS(current_app.config['SECRET_KEY'])
        try :
            data = t.loads(token)
        except :
            return False

        if data.get('id') != self.id :
            return False

        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Essay(db.Model):
    __tablename__ = 'essay'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(128)) #简介
    body_html = db.Column(db.Text) #正文
    timestamp = db.Column(db.DateTime,index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Essay %r>' % (self.title)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






# def test_sql_data():
#     db.drop_all()
#
#
# if __name__ == '__main__':
#     test_sql_data()
