#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 04:28:58 PM CST
# File Name: deffunction_04.py
# Description:  扩展函数中的某个闭包，允许它能访问和修改函数的内部变量
                    通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。
                    但是可以通过编写访问函数并将其作为函数属性绑定到闭包上来实现这个目的
"""

def sample():
    n = 0

    #Closure function
    def func():
        print('n='. n)

    #Accessor method for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value


    #Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


if __name__ == "__main__":
    f = sample()
    print(f())
    f.set_n(10)
    print(f())
    print(get_n())


'''
1->  首先， nonlocal 声明可以让我们编写函数来修改内部变量的值。

2->  其次，函数属性允许我们用一种很简单的方式将访问方法绑定到闭包函数上，
        这个跟实例方法很像 (尽管并没有定义任何类)。
'''
