#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testwith.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:46:01 2019
# Description: 
#************************************************************************#


hosts = file('/etc/hosts')

try:
    for line in hosts:
        if line.startswith('#'):
            continue
        print line

finally:
    hosts.close()


print '=================================================='


#from __future__ import with_statement
with file('/etc/hosts') as hosts:
    for line in hosts:
        if line.startswith('#'):
            continue
        print line 

