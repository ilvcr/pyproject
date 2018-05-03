#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 02 May 2018 12:06:29 AM CST
# File Name: modules_and_packages_01.py
# Description:      构建一个模块的层级包
                    将代码组织成由很多分层模块构成的包
"""

'''
封装成包是很简单,在文件系统上组织你的代码，
并确保每个目录都定义了一个__init__.py 文件。

比如：
graphics/
    __init__.py
    primitive/
        __init__.py
        line.py
        fill.py
        text.py
    formats/
        __init__.py
        png.py
        jpg.py

import包的导入
import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg



#文件__init__.py 的目的是要包含不同运行级别的包的可选的初始化代码。
#绝大部分时候让__init__.py 空着。但是有些情况下可能包含代码。
举个例子，__init__.py 能够用来自动加载子模块:
# graphics/formats/__init__.py
from . import jpg
from . import png



如果执行了语句import graphics，文件 graphics/ init .py 将被导入, 建立 graphics 命名空间的内容。
像 import graphics.format.jpg 这样导入，文件 graphics/__init__.py 和文件graphics/graphics/formats/__init__.py 
将在文件 graphics/formats/jpg.py 导入之前导入。
'''
