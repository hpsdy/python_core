#!/bin/python
#-*- coding:utf-8 -*-
from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime
import re
from collections import defaultdict
max = 2147483647
tlds = ('com','edu','net','org','gov')
with open('./gendata.txt','ab') as fn:
    for i in range(randrange(5,11)):
        dtint = randrange(max)
        dtstr = ctime(dtint)
        llen = randrange(4,8)
        login = ''.join(choice(lc) for j in range(llen))
        dlen = randrange(llen,13)
        dom = ''.join(choice(lc) for j in range(dlen))
        tmp = '%s::%s@%s.%s::%d-%d-%d\n' %(dtstr,login,dom,choice(tlds),dtint,llen,dlen)
        fn.write(tmp.encode('utf-8'))

with open('./gendata.txt','rb') as fn:
    all = fn.read().decode('utf-8')
    f = r'(?im)^(mon|tue|wed|thu|fri|sat|sun).*'
    f = r'(?i)(\d+)-\d+-\d+'
    f = r'(?i)::([\w@.]+)::'
    #Fri Jul 23 19:08:34 1999::cbnvmrf@xonxyvgwe.gov::932728114-7-9
    f = r'(?im)^(?:mon|tue|wed|thu|fri|sat|sun)\s+(?:\w+)\s+\d{1,2}\s+(?:\d{1,2}:\d{1,2}:\d{1,2})\s+(?:\d{4})::([a-z]+)@(?:[a-z]+)\.(?:\w{3})::(?:\d+-\d+-\d+)'
    f = re.compile(f)
    group = re.findall(f,all)
    print(group)
    ret = defaultdict(int)
    for x in group:
        ret[x] += 1
    print(ret)




a = 12.45


def getTypeinfo(p):
    regex = r'<[\w]+\s+\'(\w+)\'>'
    regex = re.compile(regex)
    xxx = type(p)
    xxx = str(xxx)
    r = re.match(regex,xxx)
    if r is not None:
        print(r.group(1))
    else:
        print(None)


getTypeinfo(a)