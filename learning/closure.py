#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   closure.py
@Time    :   2024/04/16 01:00:14
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""

# ! 闭包：函数嵌套函
# & 构成条件：1. 函数嵌套函数 2. 函数内部引用外部函数的非全局变量 3. 外部函数返回内部函数


def outfunc():
    sum = 0

    def innerfunc(num):
        nonlocal sum
        sum += num
        return sum

    return innerfunc


# & 闭包的作用：1.保存非全局变量，但是不易被销毁改变的数据 2.装饰器 3.实现数据锁定


def outfunc():
    n = 10

    def innerfunc():
        n = 20
        print("innerfunc", n)

    print("outfunc", n)
    innerfunc()


outfunc()


def outfunc(m):
    n = 10

    def innerfunc():
        print("innerfunc", n + m)

    return innerfunc


ot = outfunc(2)
ot()


def outfunc(m):
    n = 10

    def innerfunc():
        nonlocal m
        m += 1
        print(m)

    return innerfunc


ot = outfunc(1)
ot()
