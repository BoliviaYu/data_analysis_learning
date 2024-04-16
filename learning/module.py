#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   module.py
@Time    :   2024/04/15 16:49:53
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""

# 内置模块，自动导入
import builtins

# dir 列出对象的所有属性和方法
# print(dir(builtins))

s = 100


def testa(a, b):
    print(__name__)
    return a + b
