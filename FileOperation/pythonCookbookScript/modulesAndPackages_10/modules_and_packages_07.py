#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 03 May 2018 02:57:55 PM CST
# File Name: modules_and_packages_07.py
# Description:  导入模块同时修改模块
                    问题的本质就是想在模块被加载时执行某个动作。想在一个模块被加载时触发某个回调函数来通知。
"""


#postimport.py

import importlib
import sys
from collections import defaultdict

_post_import_hooks = defaultdict(dict)

class PostImportFinder(object):
    def __init__(self):
        self._skip = set()

    def find_module(self, fullname, path=None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportFinder(self)


class PostImportLoader(self):
    def __init__(self):
        self._finder = finder


    def load_module(self, fullname):
        importlib.import_module(fullname)
        module = sys.module[fullname]
        for func in _post_import_hooks[fullname]:
            func(module)
        self._finder._skip.remove(fullname)
        return module


    def with_imported(fullname):
        def decorate(func):
            if fullname in sys,modules:
                func(sys.modules[fullname])
            else:
                _post_import_hooks[fullname].append(func)
            return func

        return decorate


sys.meta_path.insert(0, PostImportFinder())





#使用上述例子
from functools import wraps
from postimport import when_imported

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper


#Example
@when_imported('math')
def add_logging(mod):
    mod.cos = logged(mod.cos)
    mod.sin = logged(mod.sin)
