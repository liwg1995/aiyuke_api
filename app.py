#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 上午10:19
# @Author  : Wugang Li
# @File    : app.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask import Flask
from model import db
from common.public import errors
from flask_restful import Api
from api import all,test,cate

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

api = Api(app,catch_all_404s=True,errors=errors)


api.add_resource(test.Test,'/','/test')
api.add_resource(all.All,'/news')
api.add_resource(cate.Cate,'/news/cate=<string:cate>')