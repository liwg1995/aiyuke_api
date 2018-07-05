#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/7/5 上午10:50
# @Author  : Wugang Li
# @File    : public.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask import jsonify,Flask
from model import db
from flask_restful import Api,fields,reqparse


errors = {
    'AlreadyExistsError': {
        'message': "It is already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

resource_full_fields = {
    'id': fields.Integer,
    'title':fields.String,
    'source':fields.String,
    'datetime':fields.DateTime(dt_format='rfc822'),
    'content':fields.String,
    'cate':fields.String,
    'qiniu_url':fields.String
}

class Common:
    def returnTrueJson(self, data, msg="请求成功"):
        return jsonify({
            "status": 1,
            "data": data,
            "msg": msg
        })

    def returnFalseJson(self, data=None, msg="请求失败"):
        return jsonify({
            "status": 0,
            "data": data,
            "msg": msg
        })