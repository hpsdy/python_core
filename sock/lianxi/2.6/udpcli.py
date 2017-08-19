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

addr = (host,port)
sock = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input('>>')
    if data:
        sock.sendto(data.encode(),addr)
    while True:
        data,addr = sock.recvfrom(bufsize)
        if data:
            print('return data:%s' % data.decode())
            break