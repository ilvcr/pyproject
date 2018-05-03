#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 02 May 2018 12:14:47 AM CST
# File Name: modules_and_packages_02.py
# Description:  使用相对路径名导入包中子模块
                    将代码组织成包, 用 import 语句从另一个包名没有硬编码过的包的中导入子模块。
"""

'''
使用包的相对导入，使一个的模块导入同一个包的另一个模块举个例子，
    假设在文件系统上有mypackage包，组织如下：

mypackage/
    __init__.py
    A/
        __init__.py
        spam.py
        grok.py
    B/
        __init__.py
        bar.py


两个 import 语句都没包含顶层包名，而是使用了 spam.py 的相对路径。
1->
    如果模块 mypackage.A.spam 要导入同目录下的模块 grok，它应该包括的 import语句如下：
# mypackage/A/spam.py
from . import grok

2->
    如果模块 mypackage.A.spam 要导入不同目录下的模块 B.bar，它应该使用的 import 语句如下：
# mypackage/A/spam.py
from ..B import bar


在包内，既可以使用相对路径也可以使用绝对路径来导入。
# mypackage/A/spam.py
from mypackage.A import grok # OK
from . import grok # OK


import 语句指定目录名. 为当前目录， ..B 为目录../B。这种语法只适用于 import。
'''
