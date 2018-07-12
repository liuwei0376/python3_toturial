#-*- coding:utf-8 -*-
#转化为10进制
print(int('12345'))
#转化为8进制
print(int('12345',base=8))

#定义一个2进制转化函数
def int2(n,base=2):
    return int(n,base)
print(int2('1000000'))

#定义一个8进制转化函数
def int8(n,base=8):
    return int(n,base)
print(int8('12345'))

'''
functools.partial可以帮助创建一个偏函数，不需要自定义int2（），可以使用如下方式定义
2进制转化函数

本质上，functools.partial作用是，把一个函数的某些参数给固定住（即设置默认值），返回一个
新的函数，调用这个新函数会更简单。
'''
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))
print(int2('1000000',base=10))
kw={'base':2}
int('1000000',**kw)
print(int('1000000',**kw))

max2=functools.partial(max,10)
print(max2(5,6,7))

#相当于
args=(10,5,6,7)
print(max(*args))
