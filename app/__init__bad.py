#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 8:50 AM
# @Author  : onion
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from .auth import auth as auth_blueprint
from .front import front as front_blueprint
from flask_script import Manager
from flask_login import LoginManager


config_name = "Development"

app = Flask(__name__,instance_relative_config=True)
app.config.from_object(config[config_name])

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(front_blueprint)

bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)
db = SQLAlchemy(app)
manager = Manager(app)

login_manager = LoginManager(app)
login_manager.session_protection="strong"
login_manager.login_view = 'auth.login'

