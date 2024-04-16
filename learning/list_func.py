#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   list_func.py
@Time    :   2024/04/06 16:07:35
@Author  :   liam 
@Version :   1.0
@Desc    :   None
'''

li = ['a', 'b', 'c']

for i in li:
    print(i)

i = 0
while i < len(li):
    print(li[i])
    i += 1

# ! 增加

# + , insert：直接改变原列表，不会返回新的列表，插入到给的index之前

print(['python', 'help', 'java'] + [1, 2, 3])

print(['python', 'java', 'golang'].insert(1, 'C++'))  # * 这样因为没有返回新的列表，打印会是空值

li = ['python', 'c++', 'java']

t = ('c#', 'golang')

li.insert(2, t)  # type: ignore

print(li)

# append() 末尾添加

li.append('PHP')

print(li)

li.append(t)  # type:ignore

print(li)

# extend(), 会拆分obj

li.extend(('css', 'html'))
print(li)

# ! 修改元素

# 修改单个元素

nums = [1, 3, 4, 5, 10, 8, 5]
nums[2] = -10

nums[2:5] = [10, 20, 30]
print(nums)

# 插入元素，从下标为4的地方插入元素
nums[4:4] = [-1, -2, -3]

print(nums)

# ! 删除元素

# del

s = [1, 2, 3, 4, 5]
del s
s = [1, 2, 3, 4, 5]
del s[1]
del s[2:5]

# pop() 删除末尾元素，并返回该元素

s = [1, 2, 3, 4, 5]
s.pop()
s.pop(1)
print(s)

# remove() 删除第一个匹配的元素

s = [1, 2, 3, 4, 5]
s.remove(3)
print(s)

# clear() 清空列表

s = [1, 2, 3, 4, 5]
s.clear()
print(s)

# ! in, not in

# in, not in 用于判断元素是否在列表中

s = [1, 2, 3, 4, 5]
print(3 in s)
print(6 not in s)

# ! count()

# count() 统计元素出现的次数

s = [1, 2, 3, 4, 5, 3, 2, 1]
print(s.count(1))
print(s.count(2))

if s.count(3) > 0:
    print('3 is in the list')
else:
    print('3 is not in the list')

# ! reverse()

# reverse() 反转列表

s = [1, 2, 3, 4, 5]
s.reverse()
print(s)


# ! sort()

# sort() 排序列表, 默认升序, 对原列表进行修改

s = [5, 2, 3, 1, 4]
s.sort()
print(s)

s = ['python', 'java', 'c++', 'golang']
s.sort()
print(s)


# ! 列表生成式

# 列表生成式是一种简洁的创建列表的方式，可以根据某种算法生成列表。

# 语法：
# [expression for item in iterable if condition]

# 例子：

# 1. 偶数列表生成式

even_nums = [num for num in range(1, 11) if num % 2 == 0]
print(even_nums)

# 2. 平方列表生成式

squares = [num**2 for num in range(1, 11)]
print(squares)

# 3. 字符串列表生成式

s = 'hello world'
s_list = [char for char in s]
print(s_list)

# 4. 字典列表生成式

d = {'name': 'liam', 'age': 25, 'city': 'beijing'}
d_list = [(k, v) for k, v in d.items()]
print(d_list)
