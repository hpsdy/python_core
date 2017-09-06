#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
from threading import Thread
import time
from atexit import register


class num(Thread):
    handler = None
    ret = None

    def __init__(self, name, *, handler):
        super(num, self).__init__(target=self, name=name)
        self.handler = handler

    def run(self):
        if self.handler == 'fib':
            self.ret = self.fib(self, 5)
        elif self.handler == 'fac':
            self.ret = self.fac(self, 5)
        else:
            self.ret = self.sum(self, 5)
    def getResult(self):
        return self.ret
    @staticmethod
    def fib(self, n):
        time.sleep(1.2)
        if n < 2:
            return 1
        else:
            return self.fib(self, n - 2) + self.fib(self, n - 1)

    @staticmethod
    def fac(self, n):
        time.sleep(0.3)
        if n < 2:
            return 1
        return n * self.fac(self, n - 1)

    @staticmethod
    def sum(self, n):
        time.sleep(2.0)
        if n < 2:
            return 1
        return n + self.sum(self, n - 1)

@register
def _exit():
    print('i am out')
def now():
    now = time.time()
    now = time.localtime(now)
    now = time.strftime('%Y-%m-%d %H-%M-%S', now)
    print(now)


if __name__ == '__main__':
    print('normal call:')
    now()
    print(num.fib(num, 5))
    print(num.fac(num, 5))
    print(num.sum(num, 5))
    now()
    print('normal end')
    time.sleep(10)
    print('thread start')
    now()
    list = ['fib', 'fac', 'sum']
    task = []
    for cmd in list:
        task.append(num(cmd, handler=cmd))
    for _task in task:
        _task.start()
    '''
    for _task in task:
        _task.join()
        print(_task.getResult())
    '''
    now()
    print('thread end')
