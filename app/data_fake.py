#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 10:44 AM
# @Author  : onion
# @Site    : 
# @File    : data_fake.py
# @Software: PyCharm

from app.models import User,Essay
from app import db,create_app
from faker import Faker
from random import randint


def test_sql_data():
    app=create_app('Development')
    app_context =app.app_context()
    app_context.push()
    db.drop_all()
    db.create_all()
    u=User()
    u.gen_password('zhou')
    u.nickname='zhou'
    u.email='zhou@foxmail.com'
    db.session.add(u)
    db.session.commit()

def test_essay(count=100):

    app = create_app('Development')
    app_context = app.app_context()
    app_context.push()

    fake = Faker()
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        p = Essay(title=fake.text(max_nb_chars=64),
                body_html=fake.text(),
                 timestamp=fake.past_date(),
                 author=u)
        db.session.add(p)
    db.session.commit()


if __name__ == '__main__':
    test_essay()