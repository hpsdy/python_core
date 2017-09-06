#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
from threading import Thread
import functools
import time
def log(p=True):
    if p==True:
        def _log(func):
            @functools.wraps(func)
            def wrapper(x,y):
                print('start:%s' % time.ctime())
                ret = func(x,y)
                print('end:%s' % time.ctime())
                return ret
            return wrapper
    else:
        def _log(func):
            @functools.wraps(func)
            def wrapper(x,y):
                return func(x,y)
            return wrapper
    return _log

@log(False)
def x(x,y):
    i = y
    for x in range(10):
        y+=1
    return y
print(x(10,20))