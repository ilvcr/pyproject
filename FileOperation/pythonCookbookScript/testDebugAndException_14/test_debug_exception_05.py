#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 12 May 2018 08:32:07 PM CST
# File Name: test_debug_exception_05.py
# Description:  补丁操作
"""

import unittest
from unittest.mock import patch
import io
import test_debug_exception_04

sample_data = io.BytesIO(b'''\
"IBM", 91.1\r
"AA",13.25\r
"MSFT", 27.72\r
\r
''')

class Tests(unittest.TestCase):
    @patch('example.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                        {'IBM': 91.1,
                        'AA': 13.25,
                        'MSFT': 27.72})

if __name__ == '__main__':
    unittest.main()
