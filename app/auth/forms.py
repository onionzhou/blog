#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 7:53 AM
# @Author  : onion
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email,EqualTo,ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])

    nickname = StringField('昵称', validators=[
        DataRequired(), Length(1, 20,message='昵称长度为1到20个字符')])

    password = PasswordField('密码', validators=[
        DataRequired(), EqualTo('password2', message='密码必须一致')])

    password2 = PasswordField('确认密码', validators=[DataRequired()])

    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经被注册.')

    #nickname 是model里定义的字段
    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经被使用~\(≧▽≦)/~啦啦啦.')

