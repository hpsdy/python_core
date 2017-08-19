#!/bin/env python3
#-*- coding:utf-8 -*-
from twisted.internet import protocol,reactor
from time import ctime
port = 8080
class TsSer(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connect from:',clnt)
    def dataReceived(self,data):
        print('data type:%s',type(data))
        self.transport.write(('[%s] %s' % (ctime(),data.decode())).encode())

factory = protocol.Factory()
factory.protocol = TsSer
print('waiting connect comimg...')
reactor.listenTCP(port,factory)
reactor.run()

