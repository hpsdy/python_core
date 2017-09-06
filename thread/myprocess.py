#!/usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
from multiprocessing import Process,Queue,Event
q = Queue(10)
def write(e,num):
    #q.put(num)
    with e:
        print('write get event')
def read(e):
    #num = q.get()
    #print('num:%s' % num)
    with e:
        print('read get event')
e = Event()
p1 = Process(target=write,args=(e,10))
p2 = Process(target=read,args=(e,))
p1.start()
p2.start()
e.set()
q.close()
q.join_thread()
