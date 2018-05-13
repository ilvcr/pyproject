#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 10:01:49 PM CST
# File Name: test_debug_exception_07.py
# Description:  将测试输出用日志记录到文件中
"""

#希望将单元测试的输出写到到某个文件中去, 而不是打印到标准输出

import unittest
'''
运行单元测试一个常见技术就是在测试文件底部
'''

class MyTest(unittest.TestCase):
    pass



import sys

def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)

'''
if __name__ == '__main__':
    unittest.main()
'''

if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f)


