#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 10:32:06 PM CST
# File Name: concurrent_programming_19.py
# Description:  在日志文件中查找出所有访问过 robots.txt 文件的主机的脚本
"""

#findrobots.py

import gzip
import io
import glob

def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='asxii'):
            fields = line.splite()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])

    return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
        robots = find_all_robots('logs')
        for ipaddr in robots:
            print(ipaddr)

