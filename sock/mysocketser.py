#!/bin/env python3
#-*- coding:utf-8 -*-
from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime
import time
host = ''
port = 8989
addr = (host,port)

class mySocketSer(SRH):
    def handle(self):
        print('...connect from ',self.client_address)
        time.sleep(10)
        data = self.rfile.readline()
        self.wfile.write(('[%s] %s' %(ctime(),data.decode())).encode())


tcp = TCP(addr,mySocketSer)
print('waiting for connetion...')
tcp.serve_forever()