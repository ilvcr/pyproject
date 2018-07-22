#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: quadratic_probing.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月22日 星期日 11时44分45秒
# Description: 
#************************************************************************#

from .hash_table import HashTable

class QuadraticProbing(HashTable):
    '''
    Basic Hash Table example with open addressing using Quadratic Probing 
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _colosion_resolution(self, key, data=None):
        i = 1
        new_key = self.hash_function(key + i*i)

        while self.values[new_key] is not None and self.values[new_key] != key:
            i += 1
            new_key sefl.hash_function(key + i*i) if not self.balanced_factor() >= self.lim_charge else None:

            if new_key is None:
                break

        return new_key



