import sys
from . import uparse
print(uparse.a)
'''

p = sys.argv[1:]


class a(object):
    w=10
    def __init__(self, *argv):
        print('a', self.w)
        print('a:', argv)
    def read1(self):
        print('read a:',self.w)

class b(a):
    w=20
    def __init__(self, *argv):
        print('b1', self.w)
        supers = super(b, self).__init__
        supers()
        print('b2',self.w)
        print('b:', argv)
    def read(self):
        self.read1()
        print('read b:',self.w)

class c(b):
    def __init__(self):
        print('c1', self.w)
        supers = super(c, self).__init__
        supers()
        self.w=100
        print('c2',self.w)
        self.read()


c()
'''