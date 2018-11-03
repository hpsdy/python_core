#!/usr/bin/env python3
import sys,logging
logging.basicConfig(filename='/home/work/github/python_core/class/log') 
line = input()
logging.warning('type:%s,int:%s,o:%s' % (type(line),repr(line),line))
print('test',type(line),line)  
sys.stdout.flush()  
