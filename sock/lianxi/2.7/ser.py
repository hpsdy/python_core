#!/bin/env python3
# -*- coding:utf-8 -*-
from socket import *
from time import ctime
import select, queue
import re

host = 'localhost'
port = 7878
addr = (host, port)
timeout = 10000
bufsize = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
print('recv buf:%s' % sock.getsockopt(SOL_SOCKET, SO_RCVBUF))
sock.bind(addr)
sock.setblocking(False)
sock.listen(10)
fileno = sock.fileno()
# epoll
ep = select.epoll()
ep.register(fileno, select.EPOLLIN)
msg = {}
sockarr = {fileno: sock}
group = {}
fnmap = {}
while True:
    print('waiting connect coming...,time:%s' % ctime())
    events = ep.poll(timeout)
    print('getten events...,time:%s' % ctime())
    if not events:
        print('events is null')
        continue
    print('events:', events)
    for fn, even in events:
        bsock = sockarr[fn]
        xfileno = bsock.fileno()
        if bsock == sock:
            print('===新连接===')
            nsock, nddr = sock.accept()
            print('new connect coming:', nddr)
            nsock.setblocking(False)
            nfileno = nsock.fileno()
            ep.register(nfileno, select.EPOLLIN)
            msg[nfileno] = queue.Queue()
            sockarr[nfileno] = nsock
        elif even == select.EPOLLIN:
            print('===输入===')
            info = bsock.recv(bufsize)
            info = info.decode()
            print('in data:%s' % info)
            if not info:
                continue
            ret = re.search(r'(?i)group:([\w]+)\n$', info)
            if ret:
                name = ret.group(1)
                print('group name %s' % name)
                if name not in group:
                    group[name] = []
                if xfileno not in group[name]:
                    group[name].append(xfileno)
                if xfileno not in fnmap:
                    fnmap[xfileno] = name
            else:
                msg[xfileno].put(info)
                ep.modify(xfileno, select.EPOLLOUT)
        elif even == select.EPOLLOUT:
            print('===输出===')
            try:
                data = msg[xfileno].get(False)
                if not data and xfileno in fnmap and fnmap[xfileno] in group:
                    for x in group[fnmap[xfileno]]:
                        if xfileno == x:
                            continue
                        else:
                            tsock = sockarr[x]
                            tsock.sendall(('[%s] coming %s' % (tsock.getpeername(), fnmap[xfileno])).encode())
                if data:
                    if xfileno in fnmap and fnmap[xfileno] in group:
                        for x in group[fnmap[xfileno]]:
                            if xfileno == x:
                                continue
                            else:
                                tsock = sockarr[x]
                                tsock.sendall(('[%s] coming %s' % (tsock.getpeername(), data.decode())).encode())
                    else:
                        tsock = sockarr[xfileno]
                        tsock.sendall(('return data:[%s] %s' % (ctime(), data.decode())).encode())
            except Exception as e:
                print('exception:', e)
            finally:
                ep.modify(xfileno,select.EPOLLIN)
        elif even == select.EPOLLHUP:
            print('===断开===')
            client = sockarr[xfileno].getpeername()
            print(client,' close')
            ep.unregister(xfileno)
            sockarr[xfileno].close()
            del sockarr[xfileno]
            if xfileno in fnmap:
                name = fnmap[xfileno]
                del fnmap[xfileno]
                if name in group and xfileno in group[name]:
                    group[name].remove(xfileno)

ep.unregister(fileno)
ep.close()
sock.close()