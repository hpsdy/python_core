#!/bin/env python3
#-*- coding:utf-8 -*-
from socket import *
import time
host = 'localhost'
port = 8888
addr = (host,port)
bufsize = 1024
sock = socket(AF_INET,SOCK_STREAM)
sock.connect(addr)
while True:
    data = input('>>')
    print('data type:%s' % type(data))
    if not data:
        break
    sock.send(data.encode())
    data = sock.recv(bufsize)
    print('ret data type:%s' % data)
    if not data:
        break
    print(data)
sock.close()