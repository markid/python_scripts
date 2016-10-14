#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Description:
   Author: mahongwei
   Date: 2016/10/14
"""

class GreekGetter:
    def __init__(self):
        self._trans = dict(dog="σκύλος", cat="γάτα")
    def get(self, msgid):
        try:
            return self._trans[msgid]
        except KeyError:
            return str(msgid)
class EnglishGetter:
    def get(self, msgid):
        return str(msgid)

def factory(language='English'):
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

if __name__ == '__main__':
    e, g = factory(), factory('Greek')
    for msgid in "dog parrot cat bear".split():
        print e.get(msgid), g.get(msgid)