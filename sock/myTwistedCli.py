#!/bin/env python3
#-*- coding:utf-8 -*-
from twisted.internet import protocol,reactor
from time import ctime
host = 'localhost'
port = 8080
class TsCliProtocol(protocol.Protocol):
    def connectionMade(self):
        print('connecting...')
        self.senddata()
    def dataReceived(self,data):
        print('return data:%s' % data.decode())
        self.senddata()
    def senddata(self):
        data = input('>>')
        if not data:
            self.transport.loseConnection()
        else:
            self.transport.write(data.encode())

class TscliFactory(protocol.ClientFactory):
    protocol = TsCliProtocol
    clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()


reactor.connectTCP(host,port,TscliFactory())
reactor.run()
