#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: rot13.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月17日 星期二 13时55分32秒
# Description: 
#************************************************************************#


from __future__ import print_function
def decrypt(s, n):
    out = ''
    for c in s:
        if c >= 'A' and c <= 'Z':
            out += chr(ord('A') + (ord(c) - ord('A') + n) % 26)
        elif c >= 'a' and c <= 'z':
            out += chr(ord('a') + (ord(c) - ord('a') + n) % 26)
        else:
            out += c

    return out

def main():
    s0 = 'HELLO'

    s1 = dencrypt(s0, 13)
    print s1  #URYYB

    s2 = dencrypt(s1, 13)
    print s2  #HELLO


if __name__ == '__main__':
    main()


