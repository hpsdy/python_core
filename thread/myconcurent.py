#!/usr/bin/env python
# -*- coding:utf-8 -*-
from concurrent import futures
import threading
import time,random
def run(num):
    name = threading.current_thread().name
    print('cur thread name:%s' % name)
    time.sleep(num)
    print('cur thread end:%s' % name)
    return num*10

rand = [random.randint(3,6) for x in range(random.randrange(1,10,2))]
print('rand:',rand)
len = len(rand)
def smend(a):
    print('%s over' % (threading.current_thread().name),a)
task = []
with futures.ThreadPoolExecutor(len) as execor:
    '''
    for ret in execor.map(run, rand):
        print(type(ret))
    
        for num,ret in zip(rand,execor.map(run,rand)):
        print(num,ret)
    '''
    for num in rand:
        f = execor.submit(run,num)
        f.add_done_callback(smend)
        task.append(f)
for _task in task:
    print(_task.result())

