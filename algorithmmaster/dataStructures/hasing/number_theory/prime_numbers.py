#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: prime_numbers.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月22日 星期日 10时56分47秒
# Description:  module to operations with prime numbers 
#************************************************************************#

def check_prime(number):
    """
    it's not be best solution
    """
    special_non_primes = [0, 1, 2]
    if number in special_non_primes[:2]:
        return 2
    elif number == special_non_primes[-1]:
        return 3

    return all([number %i for i in range(2, number)])

def next_prime(value, factor=1, **kwargs):
    value = factor * value
    first_value_val = value

    while not check_prime(value):
        value += 1 if not ("desc" in kwargs.keys() and kwargs["desc"] is True) else -1

    if value == first_value_val:
        return next_prime(value+1, **kwargs)

    return value


