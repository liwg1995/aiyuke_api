#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 上午11:06
# @Author  : Wugang Li
# @File    : test.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_restful import Resource

class Test(Resource):
    def get(self):
        return 'Hello!'