#类方法调用
from abc import ABCMeta,abstractmethod
class test(metaclass=ABCMeta):
    w = 10
    def a(self):
        print('ret','123')
        return 1
    @staticmethod
    def x(a,b):
        print(a+b)
    @classmethod
    def y(cls):
        print(cls.w)
    @abstractmethod
    def xyz(self):
        '''xy'''
        print('hi')


'''b = test()
print(test.a(b))

print(b.a())
test.x(10,20)
test().x(10,20)
print(test.x)
print(test().x)

print(test().a == test().a)
print(b.a == b.a)
print(b.a)

print(test.y())
print(test().y())'''
class xy(test):
    def one(self):
        print(123)
        yield 123

xy()
import abc


#test()