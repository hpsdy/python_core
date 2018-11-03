#!/usr/bin/env python3
from subprocess import *
#fn=Popen('/usr/bin/python3 /home/work/github/python_core/class/t1.py',bufsize=100,stdin=PIPE,stderr=PIPE,stdout=PIPE,shell=True)
fn=Popen('/home/work/github/python_core/class/input',bufsize=100,stdin=PIPE,stderr=PIPE,stdout=PIPE,shell=True)
#fn=Popen('/home/work/github/python_core/class/input',bufsize=100,shell=True)
print(fn.stdin.write(b'10\n'))
fn.stdin.flush()
print(fn.poll())
print(fn.wait())
print(fn.stdout.read())
