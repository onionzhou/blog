#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from flask import Flask

#__init__bad ??
# from app import app,db,manager
from app.models import User,Essay
from flask_script import Shell

#__init__ok
from flask_script import  Manager
from app import  create_app,db

app = create_app("Development")
manager =Manager(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Essay=Essay)


manager.add_command("shell",Shell(make_context=make_shell_context))

'''
onion$ python blog.py shell  启动shell

onion$ python blog.py runserver -h 127.0.0.1 -p 5000 启动服务

'''
if __name__ == '__main__':
    print(app.url_map)
    manager.run()
