#!/bin/python
#-*- coding:utf-8 -*-
import re
with open('./who') as fn:
    for line in fn:
        print(re.split(r'\s\s+',line))
