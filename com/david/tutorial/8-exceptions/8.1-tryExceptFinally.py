# -*- coding:utf-8 -*-

'''
python中的错误处理机制

try ... except ... finally

python同样遵循java中的异常继承机制，所有异常的父类为BaseException,
使用except时需要注意，它不但捕获该类型异常，还把其子类一网打尽
'''

try:
    print('Try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError: ', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('Program has no error')
finally:
    print('finally...')
print('The END')


'''
记录错误堆栈使用logging
'''
import logging

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar(s):
    return foo(s)*3

def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)

main()