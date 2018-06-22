#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: key_generator_0001.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月21日 星期四 19时08分52秒
#Description:  Apple Store App 独立开发者要搞限时促销，为应用生成激活码（或者优惠券），
                    使用 Python 如何生成 200 个激活码（或者优惠券）？
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

from uuid import uuid4

def generate_key(num):
    key_list = [str(uuid4()) for i in range(num)]
    return key_list

def main():
    print generate_key(200)

if __name__ == '__main__':
    main()


