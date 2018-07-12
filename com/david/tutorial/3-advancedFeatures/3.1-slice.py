# -*- coding:utf8 -*-

'''
高级特性 - 切片
'''

#龊方法，使用循环来获取list元素
r=[]
L=['zs','lisi','ww','zl','qq']
print(range(3))
for i in range(3):
    r.append(L[i])
print(r)

#使用切片获取list中元素
print(L[0:3])
print(L[:3])#0可以省略
print(L[1:3])
print(L[-1])#支持-1取最后一个,qq

#倒数切片
print(L[-2:]) #['zl', 'qq']
print(L[-1:]) #['qq']

L=list(range(100))
print(L)
#取前10个
print(L[:10])
#取后10个
print(L[-10:])
#取前11到20个数
print(L[10:20])
#前10个数，每2个取一个
print(L[:10:2])
#取全部数,或原样复制数组
print(L[:])
print(L[::5])#0，5，。。。95

'''
高级特性 - tuple切片
tuple也是一种list，唯一区别是tuple不可变，
tuple也可以用切片操作，只是操作的结果仍是tuple
'''
print((0,1,2,3,4,5)[:3])

'''
高级特性 - str切片
字符串也是一种list
str也可以用切片操作，只是操作的结果仍是str
在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
'''
print('abcdefg'[:4])
print('abcdefg'[::2])

