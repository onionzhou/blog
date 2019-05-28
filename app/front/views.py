#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 9:27 PM
# @Author  : onion
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from flask import render_template, redirect, url_for
from app.front import front
from .forms import EssayForm
from ..models import Essay, User
from flask_login import current_user
from .. import db


@front.route('/', methods=['GET', 'POST'])
def index():
    form = EssayForm()
    if form.validate_on_submit():
        essay = Essay()
        essay.body_html=form.body.data
        essay.title=form.title.data
        essay.author = current_user._get_current_object()


        db.session.add(essay)
        db.session.commit()
        return redirect(url_for(".index"))

    essays = Essay.query.order_by(Essay.timestamp.desc()).all()

    return render_template("index.html", form=form, essays=essays)


@front.route('/user/<nickname>')
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first_or_404()
    return render_template('user.html', user=user)
