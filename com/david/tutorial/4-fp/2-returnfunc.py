#-*- coding:utf-8 -*-

def calc_sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(calc_sum(1,2,3))

def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum
f = lazy_sum(1,2,3)
print(f)
print(f())