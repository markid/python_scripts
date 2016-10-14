#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Description:
   Author: mahongwei
   Date: 2016/10/14
"""
# ----------------one method-------------
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
class MyClass(Singleton):
    a = 1
one = MyClass()
two = MyClass()
print id(one)
print id(two)
# -------------second method-----------------
class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1
# ----------------third method--------------

def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class MyClass4(object):
    a = 1

    def __init__(self, x=0):
        self.x = x