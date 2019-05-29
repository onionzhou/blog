#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 8:51 AM
# @Author  : onion
# @Site    : 
# @File    : config.py
# @Software: PyCharm


class Config(object):
    # 数据库配置
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    # 表单配置
    SECRET_KEY = "qwertyuio"

    # 邮件配置
    MAIL_SERVER = 'smtp.qq.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    #分页设置
    FLASKY_POSTS_PER_PAGE = 20

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/blog"


class ProductConfig(Config):
    pass


config = {
    "Development": DevelopConfig,
    "Product": ProductConfig
}
