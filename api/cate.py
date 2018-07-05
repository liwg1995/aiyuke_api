#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 下午2:04
# @Author  : Wugang Li
# @File    : cate.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me


from flask_restful import Resource,abort,marshal
from common.public import Common,resource_full_fields
from model import Article

class Cate(Resource):
    def get(self,cate):
        cates = Article.query.filter_by(cate=cate).all()
        if cate is not cates:
            abort(410,msg="没数据呐，哥们！",data=None,status=0)
        else:
            return Common.returnTrueJson(Common,marshal(cate,resource_full_fields))