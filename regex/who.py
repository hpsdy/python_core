#!/bin/python
#-*- coding:utf-8 -*-
import re,os
#with os.popen('who') as fn:
#    for line in fn:
#        print(re.split(r'\s\s+|\t',line.rstrip()))

regex = re.compile(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) ([\w]+)\s\s+(\d)\s\s+([\d,]+ K)')
with os.popen('tasklist /nh') as fn:
    for line in fn:
        if line.strip() is None:
            continue
        print(re.findall(regex,line))