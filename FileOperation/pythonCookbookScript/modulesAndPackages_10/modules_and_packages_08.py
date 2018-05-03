#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 03 May 2018 03:13:55 PM CST
# File Name: modules_and_packages_08.py
# Description:  分发包
"""

'''
如果想分发代码，第一件事就是给它一个唯一的名字，并且清理它的目录结构。

一个典型的函数库包会类似下面这样：
projectname/
    README.txt
    Doc/
        documentation.txt
    projectname/
        __init__.py
        foo.py
        bar.py
        utils/
            __init__.py
            spam.py
            grok.py
    examples/
        helloworld.py
        ...
'''

#要让包可以发布出去，首先要编写一个 setup.py

#setup.py
from distutils.core import setup
setup(name='projectname',
    version='1.0',
    author='Your Name',
    author_email='you@youraddress.com',
    url='http://www.you.com/projectname',
    packages=['projectname', 'projectname.utils'],
)

#下一步，就是创建一个 MANIFEST.in 文件，列出所有在你的包中需要包含进来的非源码文件：
# MANIFEST.in
include *.txt
recursive-include examples *
recursive-include Doc *


#确保 setup.py 和 MANIFEST.in 文件放在你的包的最顶级目录中,执行命令来创建一个源码分发包
% bash python3 setup.py sdist
