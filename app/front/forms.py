#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 10:43 PM
# @Author  : onion
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
#from ..models import Role, User

class EssayForm(FlaskForm):
    title =StringField("标题",validators=[DataRequired()])
    body = TextAreaField("写点什么吗？",validators=[DataRequired()])
    submit = SubmitField('提交')