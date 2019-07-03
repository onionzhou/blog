#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 8:08 PM
# @Author  : onion
# @Site    : 
# @File    : user.py
# @Software: PyCharm


from app.api import api
from ..models import User
from flask import jsonify

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

