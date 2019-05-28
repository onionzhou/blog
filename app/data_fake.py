#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 10:44 AM
# @Author  : onion
# @Site    : 
# @File    : data_fake.py
# @Software: PyCharm

from app.models import User,Essay
from app import db,create_app


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

def essay():
    bk_1 = Essay(title="人生", body="人生正文1gggg", author_id=au_1.id)
    bk_2 = Essay(title="人生2", body="人生正文2", author_id=au_1.id)
    bk_3 = Essay(title="人生3", body="人生正文3", author_id=au_2.id)
    bk_4 = Essay(title="人生4", body="人生正文4", author_id=au_2.id)
    db.session.add_all([bk_1, bk_2, bk_3, bk_4])
    db.session.commit()

if __name__ == '__main__':
    test_sql_data()