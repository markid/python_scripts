#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Description:
   Author: mahongwei
   Date: 2016/10/14
"""

class Node():
    def __init__(self, val, next=None):
        self._data = val
        self._next = next

class LinkedList():
    def __init__(self, data=None):
        if data == None:
            self.head = None
        else:
            self.head = Node(data[0])
            p = self.head
            for i in data[1:]:
                node = Node(i)
                p._next = node
                p = p._next

    def __len__(self):
        if self.head is None:
            return 0
        p = self.head
        result = 0
        while p != None:
            p = p._next
            result += 1
        return result



    def __getitem__(self, index):
        assert index >=0, 'need positive index'
        if index >= len(self):
            return None
        num = 0
        p = self.head
        while num < index:
            p = p._next
            num += 1
        return p._data

    def __setitem__(self, index, value):
        assert index >= 0, 'need positive index'
        if index >= len(self):
            return None
        if self.head is None:
            return
        p = self.head
        j = 0
        while j < index:
            p = p.next
            j += 1
        p.data = value

    def is_empty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def insert(self, index, value):
        assert index >= 0, 'need positive index'
        if index >= len(self):
            return None
        if self.head is None:
            return
        if index == 0:
            q = Node(value, self.head)
            self.head = q
            return
        p = self.head
        j = 0
        while j < index:
            p = p._next
            j += 1
        q = p._next
        s = Node(value, q)
        p._next = s


    def delete(self, index):
        if index < 0 or index >= len(self):
            return None
        if self.head is None:
            return None
        if index == 0:
            result = self.head.data
            self.head = self.head.next
            return result
        p = self.head
        j = 0
        while j < index - 1:
            p = p._next
            j += 1
        result = p._next._data
        p._next = p._next._next
        return result





