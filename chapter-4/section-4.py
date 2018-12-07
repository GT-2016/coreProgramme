# coding:utf-8
"""
第4章 python对象
"""

def func_4_5():
    fool = 4.3
    foo2 = 4.3
    print fool is foo2
    foo3 = 1.2+3.1
    print fool is foo3
    print id(fool)
    print id(foo2)
    print id(foo3)

def func_4_6():
    import types
    print dir(types)

def exercise_4_9():
    a = 10
    b = 10
    c = 100
    d = 100
    e = 10.0
    f = 10.0
    print a is b
    print c is d
    print e is f

if __name__ == '__main__':
    exercise_4_9()
