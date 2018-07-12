#-*- coding:utf-8 -*-

# 1. dict 字典

#字典查询迅速的原因：
'''
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快
'''
d = {'david':100, 'dove':98,'pidan':97}
print(d['david'])
print(d['dove'])
print(d['pidan'])

'''
如上，把数据存入dict的方法，除了初始化时制定外，还可以通过key赋值放入：
'''
d['lily'] = 89
d['lucy'] = 88
print(d)

'''
因为一个key智能对应一个value，多次对同一个key赋值多次，后面的值将把前面的赋值冲掉
'''
d['smith'] = 70
print(d['smith'])
d['smith'] = 60
print(d['smith'])

'''
key不存在，字典将报错
'''
#print(d['hahaha'])

'''
避免key不存在，有2个方法
'''
#1. 通过in判断key是否存在
print('david' in d)
print('hahaha' in d)
#2. 通过dict提供的get()方法,如果key不存在，可以返回系统默认None值，或者自定义value值；
print(d.get('david'))
print(d.get('hahaha'))
print(d.get('hahaha',-1))

'''
删除key，使用pop(key)方法，对应的value值也将从dict中删除
'''
d.pop('david')
print(d)

# 2. set 集合
'''
set与dist类似，是一组key的集合，但不存储value。
set中，没有重复的key

创建set，需要提供一个list作为输入集合
'''
s = set([1,2,3])
print(s)

#重复元素在set中自动被过滤
s = set([1,1,1,2,2,2,3,3])
print(s)
s.add(4)
print(s)

#删除yuansu
s.remove(2)
print(s)

s1 = ([1,2,3])
s2 = ([2,3,4])
print(s1 & s2)
