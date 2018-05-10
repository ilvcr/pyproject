#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 10:39:33 PM CST
# File Name: concurrent_programming_20.py
# Description:  使用多核 CPU在日志文件中查找出所有访问过 robots.txt 文件的主机的脚本
"""

#findrobots.py

import gzip
import io
import glob
from concurrent import futures

def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file
    '''

    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as Pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)
