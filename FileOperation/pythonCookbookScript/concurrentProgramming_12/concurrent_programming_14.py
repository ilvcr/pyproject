#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 07:12:56 PM CST
# File Name: concurrent_programming_14.py
# Description:  在多线程中安全的使用 LazyConnection 实例
"""

from functools import partial

def test(conn):
    with conn as s:
        s.send(b'GET /index.html/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')

        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))


    print('Got {} bytes'.format(len(resp)))


if __name__ == '__mian__':
    conn = LazyConnection(('www.python.org', 80))


    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


