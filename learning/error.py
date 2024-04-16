#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   error.py
@Time    :   2024/04/15 14:52:13
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""

# ! 异常处理
# & 语法格式一: try: except:
try:
    print(a)
except:  # 默认基类异常
    print("error")

try:
    print(a)
except NameError as e:  # 捕获异常
    print(e)

try:
    print(a)
except Exception as e:  # 捕获任意异常
    print(e)

# 多分支异常
try:
    print(a)
except IndexError as e:
    print(e)
except NameError as e:
    print(e)
except KeyError as e:
    print(e)

# & 语法格式二: try: except: else:
dic = {"name": "liam"}
try:
    print(dic["name"])
except:
    print("error")
else:
    print("success")

# & 语法格式三：try: except: finally:
try:
    print(a)
except Exception as e:
    print(f"出现错误：{e}")
finally:
    print("hhhhh")

# & 语法格式四：try: except: else: finally:
try:
    n = int(input("输入一个整数："))
    print(10 / n)
except ValueError:
    print("请输入正确的数据")
except Exception as e:
    print(f"未知错误：{e}")
else:
    print("没有异常时执行下面的代码")
finally:
    print("无论是否错误都执行下面的代码")

# ! 异常传递：在主函数中设置‘异常捕获’，调用子函数


def funa():
    return int(input("请输入整数："))


def funb():
    return funa()


try:
    print(funb())
except Exception as e:
    print(f"错误：{e}")


# ! 抛出异常
# & 主动抛出异常的步骤：1.创建Exception对象 2.raise抛出这个对象


def user():
    pwd = input("请输入密码：")
    if len(pwd) >= 6:
        return pwd
    ex = Exception("密码长度不够")
    raise ex


try:
    upwd = user()
    print(upwd)
except Exception as e:
    print(f"错误：{e}")
