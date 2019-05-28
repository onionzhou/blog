#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 8:54 PM
# @Author  : onion
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from flask import render_template,url_for,redirect,flash,request
from app.auth import auth
from app.auth.forms import LoginForm,RegisterForm
from ..models import User,db
from flask_login import login_user,logout_user,login_required,current_user
from ..send_email  import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('front.index')
            return redirect(next)
        flash('无效的用户名或密码.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("你已经退出登陆")
    return redirect(url_for('front.index'))


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form =RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.nickname = form.nickname.data
        user.gen_password(form.password.data)
        user.email=form.email.data
        db.session.add(user)
        db.session.commit()

        token =user.gen_confirm_token()
        send_email(user.email, '博客账户确认',
                   'email_confirm', user=user, token=token)
        flash('已经发送确认邮件，请查收 --。- ~~.')
        #flash('成功注册')
        # login_user(user)
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('front.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('front.index'))

