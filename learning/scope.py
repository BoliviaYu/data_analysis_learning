#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   scope.py
@Time    :   2024/04/15 12:59:46
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""

# 作用域：变量的作用范围， 清除绑定关系：del

a = 1

# & python查找变量的顺序：局部变量 -> 全局变量 -> 内置变量

# 不可变对象变量
a = 1


def funa():  # type: ignore
    global a
    print(a)
    a = 2


funa()
print(a)


# 可变对象变量
list1 = [1, 2, 3, 4]


def funlist():
    list1[0] = 5
    print(list1)


funlist()

a = 10


def funa():
    a = 1

    def funb():
        nonlocal a  # ? 用的a是外层的局部变量，a = 1这个变量
        print(f"funb函数中的a的值{a}")
        a = 2

    funb()
    print(f"funa函数中a的值{a}")


funa()
print(a)

# ! 匿名函数

# 求和函数


def sum(a, b):
    return a + b


fun_sum = lambda a, b: a + b
print(sum(1, 2))
print(fun_sum(1, 2))

# ! 三目运算符
print(1 if 1 > 2 else 2)
func = lambda x, y: x if x > y else y
print(func(1, 2))

# ! 内置函数
# & zip函数: 将多个可迭代对象打包成元组
# & map函数: 将函数应用到可迭代对象上

li = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, li)))

# & reduce函数: 将函数作用于可迭代对象上
from functools import reduce

print(reduce(lambda x, y: x + y, li))

# & enumerate函数: 将可迭代对象打包成元组
for i, v in enumerate(li):
    print(i, v)

# & filter函数: 将函数作用于可迭代对象上, 返回满足条件的元素
print(list(filter(lambda x: x % 2 == 0, li)))


# & 拆包: 将可迭代对象拆包成多个变量
def test():
    a = 10
    b = 20
    c = 30
    return a, b, c


print(test())
a1, b1, c1 = test()
print(a1, b1, c1)

tu = (1, 2, 3, 4)
a, *c, b = tu
print(f"a:{a}, c:{c}, b:{b}")
