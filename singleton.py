# coding: utf-8

'''
author: runforever
'''


class Singleton(type):

    _singleton_ins = None

    def __call__(cls, *args, **kwargs):
        if not cls._singleton_ins:
            cls._singleton_ins = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._singleton_ins


class Foo(object):
    __metaclass__ = Singleton


class Bar(object):
    __metaclass__ = Singleton


foo1 = Foo()
foo2 = Foo()

bar1 = Bar()
bar2 = Bar()

for i in (foo1, foo2, bar1, bar2):
    print id(i)
