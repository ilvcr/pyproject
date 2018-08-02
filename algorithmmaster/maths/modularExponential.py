#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: modularExponential.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年08月02日 星期四 19时38分11秒
# Description: 
#************************************************************************#

def modularExponential(base, power, mod):
    if power < 0:
        return -1
    base %= mod
    result = 1

    while power > 0:
        if power & 1:
            result = (result * base) % mod
        
        power = power >> 1
        base = (base * base) % mod

    return result


def main():
    print(modularExponential(3, 200, 13))


if __name__ == '__main__':
    main()



