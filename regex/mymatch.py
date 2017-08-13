#!/bin/python
#-*- coding:utf-8 -*-
import re
#m = re.match('[\w][\d]$','a1sd123dasd')
#print(m.group())
m = re.match('foo','foo')
w = re.search('(a(b))[\d]?','Ab3',re.I)
if m is not None:
    print(w.groups())
    print(w.group(0))
    print(w.group(1))
    print(w.group(2))


filter = r"([\w])1([\w])"
str = 'a1sd1sadasdasdas'
m = re.findall(filter,str,re.I)
w = re.finditer(filter,str,re.I)
print(m)
if m is not None:
    print(m)
for x in w:
    print(x.group())
data = [
    'Moude Qin, CA 12343',
    'Sunjkasd, CA',
    'Los Alosda, 32451',
    'Sfwfdsdc, 41353',
    'Adsd Ajsd CA'
]
for str in data:
    print(re.split(' (?=(\d{5}|[A-Z]{2}))',str))
    print(re.split(' (?=\d{5}|[A-Z]{2})', str))

f = r'''(?x)
(?P<xas>\d{3})
[ ]
(\d{3})
'''
str = '123 321'
r = re.match(f,str)
print(r.groups())
f = r'(?i)(^th.*)'
print(re.findall(f,'''the asdsa thw,
tha sadas,
 dasd Thq thwe'''))

print(re.match(r'((x)|y)(?(2)y|x)','yx'))