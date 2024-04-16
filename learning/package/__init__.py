#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2024/04/16 00:16:17
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""
from package import test1, test2

print("This is package __init__.py")

# ! 定义 * 的范围
__all__ = ["test1", "test2"]
