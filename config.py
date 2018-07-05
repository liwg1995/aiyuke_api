#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 上午10:19
# @Author  : Wugang Li
# @File    : config.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

HOST = "127.0.0.1"
DB_NAME = "aiyuke"
DB_USER = "root"
DB_PASSWD = "root"

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWD + "@" + HOST + '/' + DB_NAME