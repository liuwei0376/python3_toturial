# -*- coding:utf-8 -*-

print(sorted([36,5,-1,17,-19]))

#sorted()是高阶函数，可以接收一个key函数来实现自定义排序
print(sorted([36,5,-1,17,-19],key=abs))

#字符串排序
print(sorted(['bob','about','Zoo','Credit']))

#字符串排序,忽略大小写
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))

#字符串排序,忽略大小写,并反响排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))

##练习题
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
def sorted_by_name(t):
    return t[0]
print(sorted(L,key=sorted_by_name))
#按成绩排序
def sorted_by_score(t):
    return -t[1]
print(sorted(L,key=sorted_by_score))