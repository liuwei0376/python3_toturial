# -*- coding:utf-8 -*-

dict = {'a': 1, 'b': 2, 'c': 3}

print('-------keys-------')
for key in dict.keys():
    print(key)

print('-------values-------')
for value in dict.values():
    print(value)

print('--------k,v--------')
for k, v in dict.items():
    print('k=%s,v=%d' % (k, v))

'''
判断对象是可迭代对象的方法
'''
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance(123,Iterable))
print(isinstance({'k1':'v1','k2':'v2'},Iterable))

'''
对list元素实现类似java的下表循环
'''
for i,v in enumerate(['a','b','c']):
    print('k=%s, v=%s' % (i,v))

'''
for循环里，同时引入多个变量，下里中为2个
'''
for x,y in [(1,1),(2,2),(3,3)]:
    print('x=%s, y=%s' % (x,y))