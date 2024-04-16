#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   func_func.py
@Time    :   2024/04/12 13:37:19
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""


def funca():
    a = 5
    b = [1, 2, 3]
    c = {"a": 1, "b": 2}
    return a, b, c


fn = funca()
print(fn)


def func(*args, **kwargs):
    print(args)
    print(kwargs)
    return args, kwargs
    """
    一个接受可变位置参数和可变关键字参数的函数。
    
    参数:
    *args: 可变位置参数，表示函数可以接受任意数量的位置参数。
    **kwargs: 可变关键字参数，表示函数可以接受任意关键字参数。
    
    返回值:
    tuple: 包含传入的所有位置参数和关键字参数的元组。
    """


func(1, 2, 3, a=4, b=5)

# ! 拓展：命名关键字参数


def person(name, age, *, city="hongkong", job="coder"):
    print(name, age, city, job)


# ? *表示之后的参数必须是关键字参数，/表示之前的参数必须是位置参数

person("liam", 18, city="shanghai", job="doctor")

# ! 混合参数
# 参数定义顺序：必选参数（位置参数）、默认参数、可变参数、命名关键字参数（key=value）、关键字参数


def funa(a, b=10, *c, d=55):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    print(f"d={d}")


funa(1, 2, 3, 4, 5, 6)  # ? 这里d还是55,因为没有key=value的形式的传参
