#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
fn = open('./read.txt','ab')
a = 'abcdefghijklmnopqrstuvwxyz'
A = a.upper()
n = '0123456789'
gbk = '的一国在人了有中是年和大业不为发会工经'
len = len(gbk)-1
str = ''
for i in range(1000):
    str+=gbk[random.randint(0,len)]


import collections
arr = collections.Counter(str)
print(arr)
print(arr.values())
print(sum(arr.values()))
print(arr.most_common()[:-5:-1])