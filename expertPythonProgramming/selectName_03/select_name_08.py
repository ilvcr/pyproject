#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 01:15:16 PM CST
# File Name: select_name_08.py
# Description:  一个类有个run_script方法被替换成简化的run命令，内建的Deprecation Warning一场可以和
                    warnings模块一起被用在中间结果中
"""


class Someclass_1(object):
    def run_script(self, script, context):
        print 'doing the work'

import warnings
class Someclass_2(object):
    def run_script(self, script, context):
        warnings.warn(("'run_script' will be replaced by 'run' in version 2"),DeprecationWarning)

        return self.run(script, context)


    def run(self, script, context=None):
        print 'doing the work'

class Someclass_3(object):
    def run(self, script, context=None):
        print 'doing this work'

print Someclass_2().run_script('a script', {})

print Someclass_1().run_script('a script', {})



