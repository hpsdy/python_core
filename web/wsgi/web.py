#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from os import environ
def app(environ,start_reponse):
    start_reponse('200 OK',[('Content-Type','text/html')])
    return [b'<h1>hello qinhan</h1>']

httpd = make_server('',8888,app)
print('server at 8888 start...')
httpd.serve_forever()