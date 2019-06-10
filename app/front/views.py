#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 9:27 PM
# @Author  : onion
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from flask import render_template, redirect, url_for, request, current_app, flash
from app.front import front
from .forms import EssayForm, CommentForm
from ..models import Essay, User, Comment
from flask_login import current_user, login_required
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



@front.route('/post/<int:id>', methods=['GET', 'POST'])
def post_essay(id):
    essay = Essay.query.get_or_404(id)
    front_essay = Essay.query.get_or_404(id-1)
    back_essay = Essay.query.get_or_404(id+1)
    return render_template('info.html',essay=essay,front_essay=front_essay,back_essay=back_essay)

# def post_essay(id):
#     essay = Essay.query.get_or_404(id)
#     form = CommentForm()
#
#     if form.validate_on_submit():
#         comment = Comment(body_html=form.body.data,
#                           essay=essay,
#                           )
#         db.session.add(comment)
#         db.session.commit()
#         flash('评论已经更新.')
#         return redirect(url_for('.post_essay', id=essay.id, page=-1))
#
#     page = request.args.get('page', 1, type=int)
#     pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(
#         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#         error_out=False)
#     comments = pagination.items
#
#     return render_template('post.html', essays=[essay], comments=comments,
#                            pagination=pagination, form=form)


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


@front.route('/about')
def about():
    print("about me  ")
    return render_template('about.html')


@front.route('/blog_list')
def blog_list():
    print('list  html ')
    return render_template('list.html')


@front.route('/life')
def life():
    print("life")
    return render_template('life.html')


@front.route('/timesheet')
def timesheet():
    essays =Essay.query.all()
    for i in essays:
        print(i.title)
    print("dsdddd")
    return render_template('time.html',essays=essays)

@front.route('/leave_message')
def leave_message():
    return render_template('gbook.html')

@front.route('/info')
def info():
    return render_template('info.html')

@front.route('/index_old',methods=['GET','POST'])
def index_old():
    return render_template('index_old.html')
