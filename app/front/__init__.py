#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 9:58 PM
# @Author  : onion
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

front = Blueprint('front',__name__)

from . import  views