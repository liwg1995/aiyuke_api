#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 上午10:19
# @Author  : Wugang Li
# @File    : migrate.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask import Flask
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from model import db

app = Flask(__name__)
app.config.from_object("config")

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()