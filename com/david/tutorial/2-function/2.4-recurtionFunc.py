# -*- coding:utf-8 -*-

#顶一个阶乘函数
# fact(n) = n * fact(n-1)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))
print(fact(100))
#调用栈深度不宜过大，RecursionError: maximum recursion depth exceeded in comparison
#print(fact(1000))

#尾递归是没有表达式的
#尾递归优化后，栈只有一个，无论调用多少次都不会溢出。
#目前python并无尾递归特性
def fact2(n):
    return fact_iter(n,1)

#如下尾递归
def fact_iter(n, producer):
    if n == 1:
        return producer
    print('===>fact_item(',n-1,',',n*producer,')')
    return fact_iter(n-1,n*producer)

print(fact_iter(5,1))