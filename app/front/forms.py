#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 10:43 PM
# @Author  : onion
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField

class EssayForm(FlaskForm):
    title =StringField("标题",validators=[DataRequired()])
    # body = TextAreaField("写点什么吗？",validators=[DataRequired()])
    body = PageDownField("写点什么吗？", validators=[DataRequired()])
    submit = SubmitField('提交')

class CommentForm(FlaskForm):
    # body = TextAreaField("写点什么吗？",validators=[DataRequired()])
    body = PageDownField("来点意见？", validators=[DataRequired()])
    submit = SubmitField('提交')

class DiscussForm(FlaskForm):
    body = TextAreaField("留个小脚印？",validators=[DataRequired()])
    # body = PageDownField("来点意见？", validators=[DataRequired()])
    submit = SubmitField('提交')

