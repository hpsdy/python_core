#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
from http.server import CGIHTTPRequestHandler,test
params = sys.argv
port = params[1]
if port.isdigit():
    port = int(port)
    test(CGIHTTPRequestHandler,port=port)
else:
    print("some error")
