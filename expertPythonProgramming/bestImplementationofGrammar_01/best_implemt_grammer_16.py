#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 03:12:56 PM CST
# File Name: best_implemt_grammer_16.py
# Description:  代理装饰器使用一个全局机制来标记和注册函数
"""

#一个根据当前用户保护代码访问的安全曾可以使用一个集中检查和相关的可调用对象要求的权限来实现

class User(object):
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    pass


def protect(role):
    def _protect(function):
        def __protect(*args, **kwargs):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("I won't tell you")
            return function(*args, **kwargs)

        return __protect
    return _protect


tarek = User(('admin', 'user'))

bill = User(('user',))

class MySecrets(object):
    @protect('admin')
    def waffle_recipe(self):
        print 'use tons of butter!!'


these_are = MySecrets()
user = tarek
print these_are.waffle_recipe()

user = bill
print these_are.waffle_recipe()


