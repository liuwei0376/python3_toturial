# -*- coding:utf-8 -*-

'''
列表生成式：
list comprehensions
是python中简单、强大的用来创建list的生成式

语法结构：
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
'''

# 计算y^3
rst = [y * y * y for y in range(1, 11)]
print('rst=%s' % rst)

# 计算y^3中的偶数，组成一个list
evenlist = [x * x for x in range(1, 11) if x % 2 == 0]
print('evenlist=%s' % evenlist)

# 2层循环，可以生成全排列
print([m + n for m in 'ABC' for n in '123'])

# 利用列表生成式，列出当前目录下所有的文件和目录名
import os

list = [d for d in os.listdir('.')]
print('list=%s' % list)

# 利用列表生成式，以2个变量生成list
dict = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
dictList = [k + '=' + v for k, v in dict.items()]
print('dictList=%s' % dictList)

# 利用列表生成式，将单词全部转为大、小写
L = ['Hello', 'David', 'This', 'Is', 'Dove', 'SPEAKING']
wordUpperCase = [(k.upper(), k.lower()) for k in L]
print('wordUpperCase=%s' % wordUpperCase)

#
L1 = ['Hello', 'World', 18, 'Apple', None]
strFormat=[item for item in L1 if isinstance(item,str)]
intFormat=[item for item in L1 if isinstance(item,int)]
print('strFormat=%s' % strFormat)
print('intFormat=%s' % intFormat)
