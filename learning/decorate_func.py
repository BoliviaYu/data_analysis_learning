#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   decorate_func.py
@Time    :   2024/04/16 12:51:24
@Author  :   liam 
@Version :   1.0
@Desc    :   None
"""


# ! 装饰器模板
def wrapper(func):
    def inner(*args, **kwargs):
        print("before")
        ret = func(*args, **kwargs)
        print("after")
        return ret

    return inner


# & 日志打印器

import functools
import logging


def logger(logger=None, level=logging.INFO, log_file="app.log"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal logger
            if logger is None:
                logger = logging.getLogger(func.__module__)
            logger.setLevel(level)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            try:
                msg = f'Function "{func.__name__}" called'
                logger.log(level, msg)
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(e)
                raise e

        return wrapper

    return decorator


@logger(level=logging.INFO)
def test(x, y):
    return x / y


print(test(2, 1))
