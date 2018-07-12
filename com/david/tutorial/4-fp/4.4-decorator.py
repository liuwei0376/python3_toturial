# -*- coding:utf-8 -*-

'''
装饰器
'''


def now():
    print '2018-07-11'


f = now
f
f()

'''
函数对象有一个__name__属性，可以拿到函数名字
'''
print('------------------------')
print(now.__name__)
print(f.__name__)

'''
增强now()函数的功能，比如在函数调用前后打印日志，但不希望修改now()函数的定义，
这种在运行期动态添加功能的方式，称之为“装饰器”
'''
print('------------------------')

def log(func):
    def wrapper(*args, **kwargs):
        print("call function %s()" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


'''
如上log，为一个decorator，它可以接收一个函数作为参数，并返回一个函数。
借助python的@语法，把decorator放在函数的定义处。
'''


@log
def now():
    print('2018-07-11')


now()

'''
如果decorator本身需要传入参数，就需要编写一个返回decorator的高阶函数，比如要定义log的文本：
'''
print('------------------------')
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator
#这个三层嵌套的装饰器用法如下：
@log('execute')
def now():
    print '2018-07-11'
now()
print(now.__name__)