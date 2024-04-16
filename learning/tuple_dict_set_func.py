#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   tuple_dict_set_func.py
@Time    :   2024/04/09 15:25:26
@Author  :   liam 
@Version :   1.0
@Desc    :   None
'''

# ! tuple 元素不可修改，不可删除，可进行切片操作，元素被小括号包围
# 意义：元组是不可变的序列，提高代码安全性

num_tuple = (1, 2, 3, 4, 5)
print(num_tuple[0:3])  # (1, 2, 3)

# 通过下标访问元素
print(num_tuple[0])  # 1

# 通过index()方法访问元素的索引位置
print(num_tuple.index(3))  # 2

# count()方法统计元组中某个元素出现的次数
print(num_tuple.count(3))  # 1

# 元组可变的情况
t2 = (1, 2, 3, [4, 5, 6], 7)
print(t2[3])
t2[3][0] = 10086
print(t2)  # (1, 2, 3, ['hello', 5, 6], 7)

# ! dict 键值对是无序的，可进行切片操作，元素被花括号包围
# 意义：字典是可变的序列，存储键值对，键必须是不可变对象，值可以是任意对象

# 创建字典
# 符号大括号{}，键值对之间用冒号:分隔，键值对之间用逗号,分隔
dict1 = {'name': 'liam', 'age': 25, 'gender': 'Male', 'city': 'beijing'}
dict2 = dict()
dict3 = {}

# 增加、修改、删除字典元素
dict1['age'] = 26
dict1['email'] = 'liam@example.com'
print(dict1)

# * dict1.clear()  # 清空字典

# 查找字典元素
print(dict1.get('name'))  # liam
print(dict1.get('email'))  # None
print(len(dict1))

print(dict1.keys(), dict1.values(), dict1.items())

# 字典的遍历
for key in dict1.keys():
    print(key, dict1[key])
for value in dict1.values():
    print(value)
for key, value in dict1.items():
    print(f'{key}: {value}')

# ! set 集合是无序的，不可进行切片操作，元素被花括号包围
# 意义：集合是可变的序列，存储不重复的元素，元素可以是任意对象，元素可以是不可变对象
# 集合的元素必须是不可变的，如字符串、数字、元组，不能是列表、字典等可变的对象

# 创建集合
set1 = {1, 2, 3, 4, 5, (1, 2)}
set2 = set()
set3 = {}  # 这样创建的是字典

# 增加、修改、删除集合元素
set1.add(6)

# update() 追加数据必须是可迭代对象，可以去重
set1.update([7, 8, 9])
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

# remove() 删除元素，不存在则报错
set1.remove(3)
print(set1)
set1.discard(3)
print(set1)
set1.pop()
print(set1)

# & | ^ -
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)
print(set1 | set2)
print(set1 ^ set2)
print(set1 - set2)

# ! 公共操作
# 1) + 拼接
str1 = "hello"
str2 = "world"
print(str1 + str2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)

# 2) * 复制
print(str1 * 3)
print(list1 * 3)
print(tuple1 * 3)

# 3) in 判断 not in
print(1 in list1)
print(1 in tuple1)
print(1 in set1)

# 4) len 长度
print(len(str1))
print(len(list1))
print(len(tuple1))
print(len(set1))

# 5) max 最大值
print(max(str1))
print(max(list1))
print(max(tuple1))
print(max(set1))

# 6) range 范围
print(range(10))

# 7) enumerate 枚举
for i, v in enumerate(str1):
    print(i, v)
dict1 = {'a': 1, 'b': 2, 'c': 3}
for i, v in enumerate(dict1):
    print(i, v)

# ! 推导式
t1 = (i for i in range(10))
print(tuple(t1))

dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)
