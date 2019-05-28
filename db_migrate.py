#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 4:16 PM
# @Author  : onion
# @Site    : 
# @File    : db_migrate.py
# @Software: PyCharm

from  flask_migrate import  Migrate,MigrateCommand
from  flask_script import Manager
from app import  db,create_app
app =create_app('Development')

migrate = Migrate(app,db)

manager =Manager(app)

manager.add_command("db",MigrateCommand)

'''
初始化，创建migrations文件夹，所有迁移文件都在里面
onion$ python db_migrate.py db init

onion$ python db_migrate.py db migrate -m "init migration"
更新
onion$ python db_migrate.py db upgrade
查看历史
onion$ python db_migrate.py  db history
回退
onion$ python db_migrate.py  db downgrade 2e4130fa1864

'''


if __name__ == '__main__':
    manager.run()