#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 7:28 PM
# @Author  : onion
# @Site    : 
# @File    : essay.py
# @Software: PyCharm
from ..models import Essay
from flask import  request ,jsonify,g
from .. import db
from flask_login import login_required


from app.api import api
@api.route('/posts/',methods=['POST'])
@login_required
def add_essay():
    essay =Essay.from_json(request.json)
    essay.author =g.current_user
    db.session.add(essay)
    db.session.commit()
    return jsonify(essay.to_json())

@api.route('/posts/')
def get_essays():
    essays = Essay.query.all()
    print(essays)
    return jsonify({'essays':[essay.to_json() for essay in essays]})


@api.route('/posts/<int:id>')
def get_essay(id):
    essay = Essay.query.get_or_404(id)
    return jsonify(essay.to_json)

@api.route('/get_comments/')
def get_essay_comments():
    pass
