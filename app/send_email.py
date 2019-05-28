#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 7:23 AM
# @Author  : onion
# @Site    : 
# @File    : email.py
# @Software: PyCharm

from flask_mail import Message
from . import mail
from  flask import current_app, render_template
from threading import Thread


def _send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    t = Thread(target=_send_async_email, args=[app, msg])
    t.start()
    return t
