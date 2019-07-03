#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 7:18 PM
# @Author  : onion
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Blueprint

api = Blueprint('api',__name__)

from . import essay,user