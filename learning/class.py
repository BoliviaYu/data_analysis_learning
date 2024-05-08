#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   class.py
@Time    :   2024/04/17 01:07:12
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course):
        print("%s正在学习%s" % (self.name, course))

    def play(self):
        print("%s正在玩耍" % self.name)

    def __str__(self):
        return "姓名：%s，年龄：%s" % (self.name, self.age)

    def __del__(self):
        print("销毁对象")


class Robot(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name}只能平地行走，遇到障碍物会摔倒")

    def produce(self):
        print(f"{self.age}年生产的机器人，名字是{self.name}")


rot = Robot("罗马一代", 2000)
rot.walk()
rot.produce()


class Robot2(Robot):
    def walk(self):
        print(f"{self.name}可以避开障碍物")


rot2 = Robot2("罗马二代", 2001)
rot2.walk()
rot2.produce()


class Robot3(Robot2):
    def run(self):
        print(f"{self.name}可以快速奔跑")


rot3 = Robot3("罗马三代", 2002)
rot3.run()
rot3.produce()


# ! 类方法


class Person:
    age = 20

    @classmethod
    def human(cls):
        print(f"{cls.age}")


Person.human()
p = Person()
p.human()
