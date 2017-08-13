#!/bin/python
#-*- coding:utf-8 -*-
import re,os
with os.popen('who') as fn:
    for line in fn:
        print(re.split(r'\s\s+|\t',line.rstrip()))
