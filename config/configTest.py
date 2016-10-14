#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Description:
   Author: mahongwei
   Date: 2016/10/14
"""
import ConfigParser
conf = ConfigParser.ConfigParser()
conf.read('format.conf')
print conf.get('db1', 'conn_str')
#print conf.get('DEFAULT','conn_str')