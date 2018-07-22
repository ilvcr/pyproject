#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: double_hash.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月22日 星期日 11时04分16秒
# Description: 
#************************************************************************#


from .hash_table import HashTable
from number_theory.prime_numbers import next_prime, check_prime


class DoubleHash(HashTable):
    '''
    Hash Table example with open addressing and Double Hash
    '''
    def __init__(self, *args, **kwargs):
        super().__innit__(*args, **kwargs)

    def __hash_function_2(self, value, data):
        next_prime_gt = next_prime(value%self.size_table) \
                if not check_prime(value % self.size_table) else value % self.size_table  #gt = bigger than

        return next_prime_gt-(data%next_prime_gt)

    def __hash_double_function(self, key, data=None):
        return (increment*self.__hash_function_2(key, data)) % self.size_table

    def _colision_resolution(self, key, data=None):
        i = 1
        new_key = self.hash.hash_function(data)

        while self.calues[new_key] is not None and self.values[new_key] != key:
            new_key = self.__hash_double_function(key, data, i) if self.balances_factor(0 >= self.lim_charge else None

            if new_key is None:
                break
            else:
                i += 1

        return new_key



