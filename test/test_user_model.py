#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 8:39 PM
# @Author  : onion
# @Site    : 
# @File    : test_user_model.py
# @Software: PyCharm

from app.models import User
from app import db
import  unittest

'''
密码测试散列
'''
class UserModelTest(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_setter(self):
        u = User()
        u.gen_password("onion")
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User()
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User()
        u.gen_password("onion")
        self.assertTrue(u.verify_password('onion'))
        self.assertFalse(u.verify_password('oniononion'))

    def test_password_salts_are_random(self):
        u = User()
        u.gen_password("onion")
        u2 = User()
        u2.gen_password("onion")
        self.assertTrue(u.password_hash != u2.password_hash)

if __name__ == '__main__':
    unittest.main()
