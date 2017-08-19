#!/bin/env python3
#-*- coding:utf-8 -*-

from socket import *
import traceback
import sys
host = 'localhost'
port = 8888
bufsize = 1024
argv = sys.argv
if len(argv)==2:
    host = argv[1]
if len(argv)==3 and argv[2].isdigit():
    port = int(argv[2])
print('host:%s,port:%d' %(host,port))

sock = socket(AF_INET,SOCK_STREAM)
sock.connect((host,port))
print('cur server name:',sock.getsockname(),',remote server name:',sock.getpeername())
while True:
    try:
        data = input('>>')
        if not data:
            sock.send(data.encode())
            data = sock.recv(bufsize)
            print('return data:%s' % data.decode())
        else:
            continue
    except Exception as e:
        print(traceback.format_exc())
