#!/bin/env python3
#-*- coding:utf-8 -*-
from socket import *
import time
host = ''
port = 9999
bufsize = 1024
addr = (host,port)
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(addr)
while True:
    data,addr = sock.recvfrom(bufsize)
    print('client addr:',addr)
    sock.sendto(('[%s] %s' % (time.ctime(),data.decode())).encode(),addr)
sock.close()