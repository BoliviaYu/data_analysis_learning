#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   string_func.py
@Time    :   2024/04/03 17:30:04
@Author  :   liam 
@Version :   1.0
@Desc    :   None
'''

# ! 索引，正向索引从0开始，逆向索引负数，从-1开始

from curses.ascii import isdigit
from os import replace
from shlex import split


name = 'liam'

print(name[0], name[1], name[-1], name[-2])

# ! 字符串切片

name = 'admin_name_liam'

print(name[6:10:2], name[6:10:1], name[-1:3:-1])

# ! 字符串查找
# 1. find 子序列，检查子串是否在原来的字符串中，如果存在就返回第一次找到的索引值，否则返回-1

a = 'hello world'
print(a.find('h'))

# 2. index 查找索引，和find一样，但是如果不在原来的字符串会报错

mystr = 'hello world'
print(mystr.index('l', 0, 4))

# 3. count 查找子串在原字符串中出现的次数

mystr = 'hello world'
print(mystr.count('l', 3))

# ! 字符串修改
# 1. replace 字符串序列.replace(旧，新，替换次数)

print(mystr.replace('l', 'a', 2))

# 2. split 字符串分割

mystr = 'he,llo, wor,ld'
print(mystr.split(',', 2))

# 3. capitalize 把第一个字母大写

print(mystr.capitalize())

# 4. lower 把字符串所有大写转换为小写

print(mystr.lower())

# 5. upper 把小写变为大写

print(mystr.upper())

# 6. title 把每个单词首字母大写

print(mystr.title())

# ! 判断

# 1. islower() 检测字符串是否都是小写 isupper() 检测是否都是大写

str = 'hello python'
print(str.islower())

# 2. isdigit() 是否是数字

mystr = 'hello123'
j = 0
for i in mystr:
    if i.isdigit():
        j += 1
print(j)

# 3. startswith, endswith

print(mystr.startswith('h'))
print(mystr.endswith('3'))

# ! 增

# +

name = 'xilin'
name2 = 'li'

print(name + name2)

# join

print('*'.join('hello'))

# ! 删

# lstrip. rstrip, strip

print(' hello'.lstrip())
print('hello '.rstrip())
print(' hello world '.strip())
