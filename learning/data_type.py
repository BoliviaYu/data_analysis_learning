#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   data_type.py
@Time    :   2024/04/10 12:12:25
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""

# Python 有六种基本数据类型：
# 1.数字类型（Number）: 整数（Integer）、浮点数（Float）、复数（Complex）、Bool
# 2.字符串类型（String）
# 3.列表类型（List）
# 4.元组类型（Tuple）
# 5.字典类型（Dictionary）
# 6.集合类型（Set）

import copy

a = ["a1", "a2", "a3"]
b = ["b1", "b2", "b3"]
d = dict(zip(a, b))

# 深拷贝：完全复制
# 浅拷贝：只复制第一层，第二层是引用，应用场景——日常办公，一个表链接一个表，表内数据变动，其他表数据跟着变动

a = [1, 2, 3, [4, 5]]
a_copy = copy.copy(a)
a_deepcopy = copy.deepcopy(a)
print(id(a), id(a_copy), id(a_deepcopy))

a[0] = 5
print(a, a_copy, a_deepcopy)

a[3][0] = 6
print(a, a_copy, a_deepcopy)
