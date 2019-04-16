#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: steps_and_fbnq_problem.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 10:02:12 2019
# Description: 台阶/斐波那契问题
#************************************************************************#

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache
    return wrap


class stepAndFbnq(object):
    
    def __init__(self):
        pass

    def fib1(self, n):
        
        fib1 = lambda n: n if n <= 2 else fib1(n-1) + fib1(n-2)
        return fib1(n)

    @memo
    def fib2(self, n):
        if i < 2:
            return 1
        return fib2(n-1) + fib2(n-2)

    def fib3(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b



if __name__ == '__main__':

    sol = stepAndFbnq()
    sf1 = sol.fib1(10)
    print 'fib1 is : {} \n'.format(sf1)
    sf3 = sol.fib3(10)
    print 'fib3 is : {} \n'.format(sf3)
    sf2 = sol.fib2(10)
    print 'fib2 is : {} \n'.format(sf2)


