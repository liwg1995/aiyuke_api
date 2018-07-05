#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 上午11:09
# @Author  : Wugang Li
# @File    : all.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_restful import Resource,marshal
from common.public import Common,resource_full_fields
from model import Article


class All(Resource):
    def get(self):
        return Common.returnTrueJson(Common,marshal(Article.query.all(),resource_full_fields))



