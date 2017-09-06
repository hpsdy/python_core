#!/usr/bin/env python
#-*- coding:utf-8 -*-
import _thread
import time
from time import ctime
def loop_1(lock):
    time.sleep(2)
    lock.release(

    )
    print('loop_1')

def loop_2():
    time.sleep(4)
    print('loop_2')


if __name__=='__main__':
    print(ctime())
    lock1 = _thread.allocate_lock()
    lock1.acquire()
    lock2 = _thread.allocate_lock()
    lock2.acquire()
    _thread.start_new_thread(loop_1,(lock1,))
    _thread.start_new_thread(loop_1,(lock2,))
    lock = [lock1,lock2]
    for _lock in lock:
        while _lock.locked():
            pass
    print(ctime())