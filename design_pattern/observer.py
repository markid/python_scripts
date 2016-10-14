#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Description:
   Author: mahongwei
   Date: 2016/10/14
"""
class Subject(object):
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    def notify(self, modifier=None):
        for observer in self._observers:
            # if observer != modifier:
            #     observer.update(self)
            observer.update(self)

class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class DecimalViewer:
    def update(self, subject):
        print('HexViewer: Subject %s has data 0x%x' %
              (subject.name, subject.data))

class HexViewer:
    def update(self, subject):
        print('DecimalViewer: Subject %s has data %d' %
              (subject.name, subject.data))

if __name__ == '__main__':
    data1 = Data('Data1')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data1.data = 10
