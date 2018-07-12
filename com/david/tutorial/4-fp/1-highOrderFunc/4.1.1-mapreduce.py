# -*- coding:utf-8 -*-

'''
python内置了map()和reduce()函数
'''


# Example - 1
def f(x):
    return x * x


rst = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(rst)
print(list(rst))

# Example - 2
# 将int转换为
print(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Example - 3
# sum处理
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


# Example - 4
# 把序列[1, 3, 5, 7, 9]变换成整数13579
def func1(x, y):
    return x * 10 + y


print(reduce(func1, [1, 3, 5, 7, 9]))


# Example - 4
# 把字符串"10376"转换为数字10376
def func2(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(map(char2num, '12345'))
print(reduce(func2, map(char2num, '12345')))


# Example - 5
# 实现一个一体化函数，封装map 和 reduce函数
# 把字符串"10376"转换为数字10376
def str2int(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return digits[s]

    return reduce(fn, map(char2num, s))


print(str2int("123456"))

# Example - 6
# lambda表达式 和 reduce函数
# 把字符串"10376"转换为数字10376
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return digits[s]


print(reduce(lambda x, y: x * 10 + y,[1,2,3,4,5]))

print(list(filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', '  '])))
print(len(' '))