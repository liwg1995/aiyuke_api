#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 上午10:19
# @Author  : Wugang Li
# @File    : model.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer,unique=True,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    source = db.Column(db.String(100),nullable=False)
    datetime = db.Column(db.DateTime,nullable=False)
    content = db.Column(db.Text,nullable=False)
    cate = db.Column(db.String(100),nullable=False)
    qiniu_url = db.Column(db.String(100),nullable=False)