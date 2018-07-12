# -*- coding:utf-8 -*-
# 1. 定义函数
# 使用def语句，依次组织出函数名、括号、参数、及冒号（：）
# 然后，在缩进块中编写函数体，函数返回值用return返回。
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operater type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-33))


# 2、空函数
# 定义一个函数，什么也不做 .
# 实际上pass可以用来作为占位符，如处理逻辑还没构思好，可以先用pass来占位，语法不会报错
def my_func():
    pass


# 3、参数检查
# 调用函数时，如果参数个数不对，Python语法解释器会自动检查出来，并抛出TypeError异常：
# print(my_abs(1,2,3))

#print(my_abs('A'))


# 4、函数可以返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)

#这是一种假象，Python函数返回的仍是单一值,为一个tuple
r = move(100,100,60,math.pi/6)
print(r)