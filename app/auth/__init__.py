#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 8:53 PM
# @Author  : onion
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views

