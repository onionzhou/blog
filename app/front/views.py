#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 9:27 PM
# @Author  : onion
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from flask import render_template, redirect, url_for, request, current_app,flash
from app.front import front
from .forms import EssayForm
from ..models import Essay, User
from flask_login import current_user,login_required
from .. import db


@front.route('/', methods=['GET', 'POST'])
def index():
    form = EssayForm()
    if form.validate_on_submit():
        essay = Essay()
        essay.body_html = form.body.data
        essay.title = form.title.data
        essay.author = current_user._get_current_object()

        db.session.add(essay)
        db.session.commit()
        return redirect(url_for(".index"))

    page = request.args.get('page', 1, type=int)
    pagination = Essay.query.order_by(Essay.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    essays = pagination.items

    # essays = Essay.query.order_by(Essay.timestamp.desc()).all()

    return render_template("index.html", form=form, essays=essays,
                           pagination=pagination)


@front.route('/user/<nickname>')
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first_or_404()
    return render_template('user.html', user=user)

@front.route('/post/<int:id>')
def post_essay(id):
    essay = Essay.query.get_or_404(id)
    return render_template('post.html', essays=[essay])


@front.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_essay(id):
    essay = Essay.query.get_or_404(id)
    form = EssayForm()
    if form.validate_on_submit():
        essay.body_html = form.body.data
        db.session.add(essay)
        db.session.commit()
        flash('文章已更新.')
        return redirect(url_for('.post_essay', id=essay.id))
    form.body.data = essay.body_html
    return render_template('edit_essay.html', form=form)