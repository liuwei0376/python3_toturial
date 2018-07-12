# -*- coding:utf-8 -*-

'''
lambda表示匿名函数，冒号前的x表示函数参数
'''
rst = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('rst : %s' % rst)

# 把匿名函数赋值给一个对象
f = lambda x: x * x
print(f(5))


# 匿名函数作为返回值返回
def cube_calc(x, y):
    return lambda: x * x + y * y
print(cube_calc(3,5)())


