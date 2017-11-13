class test(object):
    def __new__(cls, *args, **kwargs):
        print(cls, *args, **kwargs)
        if not hasattr(cls,'instance'):
            print('first init')
            cls.instance = super(test,cls).__new__(cls)
        return cls.instance
    def __init__(self,num):
        print('init',self,num)
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
'''
test(1)
test(2)
test(3)
print('one',type(test(4)))
print('two',type(test))
#type.__new__()
'''

class cm(object):
    def a():
        b=100

cm.b=999
o = cm()
print(o.b)
o.b=888
print(cm.b)