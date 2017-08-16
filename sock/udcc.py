#!/bin/env python3
#-*- coding:utf-8 -*-
from socket import *
import time
host = 'localhost'
port = 9999
bufsize = 1024
addr = (host,port)
sock = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input('>>')
    if not data:
        break
    sock.sendto(data.encode(),addr)
    data,addr = sock.recvfrom(bufsize)
    print('client addr:',addr)
sock.close()