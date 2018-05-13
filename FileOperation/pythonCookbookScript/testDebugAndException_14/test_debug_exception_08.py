#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 10:13:28 PM CST
# File Name: test_debug_exception_08.py
# Description:  忽略或期望测试失效
"""

#unittest 模块有装饰器可用来控制对指定测试方法的处理
import unittest
import os
import platform


class Tests(unittest.TestCase):
    def test_0(self):
        self.assertTrue(True)


    @unittest.skip('skipped test')
    def test_1(self):
        self.fail('should have failed!')


    @unittest.skipIf(os.name=='posix', 'Not supported on Unix')
    def test_2(self):
        import winreg


    @unittest.skipUnless(platform.system()=='Darwin', 'Mac specific test')
    def test_3(self):
        self.assertTrue(True)


    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2+2, 5)


if __name__ == '__main__':
    unittest.main()


