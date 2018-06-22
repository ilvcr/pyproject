#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: create_a_table_and_put_keys_0002.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月21日 星期四 19时14分48秒
#Description: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

from uuid import uuid4
import MySQL as mdb

def generate_key(num):
    key_list = [str(uuid4()) for i in range(num)]
    return key_list

def create_a_table_and_put_keys(key_list):
    with mdb.connect('localhost', 'test', '123', 'testdb') as cur:
        #create table
        cur.execute("DROP TABLE IF EXISTS rkeys")
        cur.execute("CREATE TABLE rkeys(\
                        key_value CHAR(40) NOT NULL\
                        )")

        #insert data
        #I want to use executemany, but there is a library bug...
        # It seems that executemany cannot match single-string list
        # cur.executemany("INSERT INTO rkeys VALUES(%s)", key_list)

        for i in key_list:
            cur.execute("INSERT INTO rkeys(key_value)\
                        VALUES('%s')" % i)

def main():
    create_a_table_and_put_keys(generate_key(200))


if __name__ == '__main__':
    main()



