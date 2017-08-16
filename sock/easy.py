#!/bin/env python3
#-*- coding:utf-8 -*-
from socket import *
import time
host = ''
port = 8888
bufsize = 1024
max = 2
addr = (host,port)
sock = socket(AF_INET,SOCK_STREAM)
sock.bind(addr)
sock.listen(max)
while True:
    print('waiting alient in')
    time.sleep(10)
    cli,addr = sock.accept()
    while True:
        data = cli.recv(bufsize)
        if not data:
            break
        cli.send('[%s] %s' % (time.ctime(),data))
    cli.close()
sock.close()