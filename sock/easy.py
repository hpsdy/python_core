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
print('server:',sock)
while True:
    print('waiting alient in')
    cli,addr = sock.accept()
    print('client:',cli,' cli_addr:',addr)
    while True:
        data = cli.recv(bufsize)
        print('data type:%s' % type(data))
        if not data:
            break
        str = ('[%s] %s' % (time.ctime(),data.decode())).encode()
        print(str)
        cli.send(str)
    cli.close()
sock.close()
