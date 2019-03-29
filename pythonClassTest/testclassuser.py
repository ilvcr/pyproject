#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testclassuser.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:33:28 2019
# Description: 
#************************************************************************#

#error run


class User(object):
    def __init__(self, roles):
        self.roles = roles

class Unauthorized(Exception):
    pass

def protect(role):
    def _protect(function):
        def __protect(*args, **kw):
            user = globals().get('User')
            if user is None or role not in User.roles:
                raise Unauthorized("I won't tell you")
            return function(*args, **kw)
        return __protect
    return _protect


tarek = User(('admin', 'user'))
bill = User(('user', ))
class MySecrets(object):
    @protect('admin')
    def waffle_recipe(self):
        print 'use tons of butter!'


these_are = MySecrets()
user = tarek
print these_are.waffle_recipe()
print '==============================='
user = bill
print these_are.waffle_recipe()
print '================================'









