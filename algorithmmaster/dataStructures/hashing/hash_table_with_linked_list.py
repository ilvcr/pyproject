#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: hash_table_with_linked_list.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月22日 星期日 11时16分34秒
# Description: 
#************************************************************************#

from .hash_table import HashTable
from collections import deque

class HashTableWithLinkedList(HashTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _set_value(self, key, data):
        self.values[key] = deque([]) if self.values[key] is None else self.values[key]
        self.values[key].appendleft(data)
        self._keys[key] = self.values[key]

    def balanced_factor(self):
        return sum([self.charge_factor - len(slot) for slot in self.values]) / self.size_table * self.charge_factor

    def _colision_resolution(self, key, data=None):
        if not (len(self.values[key]) == self.charge_factor and self.values.count(None) == 0):
            return key
        return super()._colision_resolution(key, data)


