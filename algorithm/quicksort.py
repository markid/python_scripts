#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Description:
   Author: mahongwei
   Date: 2016/10/14
"""


def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x > pivot:
            greater.append(x)
        else:
            less.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)

def fib(n):
    assert n >=1, 'need a positive number'
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a+b
        i += 1

class IterTest():
    def __init__(self, l=None):
        if not l:
            self.l = []
        else:
            self.l = l
    def __iter__(self):
        return self
    def next(self):
        if not self.l:
            raise StopIteration
        else:
            return self.l.pop()


if __name__ == '__main__':
    # print '{greet} from {language}.'.format(greet='Hello world',
    #                                         language='Python')
    # input_list = [3, 2, 4, 5, 6, 7, 8]
    # #assert isinstance(set(input_list), list), "need as list"
    # print quicksort([3, 2, 4, 5, 6, 7, 8])
    # for i in fib(5):
    #     print in
    itest = IterTest(l=range(5))
    for i in itest:
        print i
    import random
    import string
    l = []
    for i in range(10):
        num = random.randint(2,5)
        l.append(random.choice(string.letters))
    print l