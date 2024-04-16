#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   module_main.py
@Time    :   2024/04/15 16:54:35
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""

import module

# 导入包的时候，__init__.py文件会被执行
import package

if __name__ == "__main__":
    print(module.s)
    print(module.testa(1, 3))
    print("This is module_main.py")

# py文件的两种功能
# 用脚本模式：__name__ == '__main__'，当作模块运行：__name__ == 模块的名字
