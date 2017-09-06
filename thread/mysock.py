#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
from threading import Thread,Lock
import time
from atexit import register
import random

class _set(set):
    def __str__(self):
        return ','.join(str(x) for x in self)
loops = (random.randrange(1,3) for num in range(random.randrange(1,10)))
arr = _set()
lock = threading.Lock()
def loop(nc):
    lock.acquire()
    ct = threading.current_thread()
    mname = ct.name
    arr.add(mname)
    print('%s start:%s' % (mname,time.ctime()))
    time.sleep(nc)
    arr.remove(mname)
    print('%s move:%s' % (mname, time.ctime()))
    print('remaing:%s' % arr)
    lock.release()
for num in loops:
    Thread(target=loop,args=(num,)).start()

for th in threading.enumerate():
    print(th)
@register
def _exit():
    print('script end:%s' % time.ctime())