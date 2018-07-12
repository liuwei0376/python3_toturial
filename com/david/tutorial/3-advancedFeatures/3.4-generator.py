# -*- coding:utf-8 -*-

from collections import Iterable

'''
生成器：

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
'''

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
rst = (m + n for m in 'AB' for n in '12')
print(next(rst))
print(next(rst))
print(next(rst))
print(next(rst))
# 抛出StopIteration的error
# print(next(rst))

# generator 也是 可迭代的
print(isinstance(rst, Iterable))

print('-------------------')
rst2 = (m + n for m in 'AB' for n in '12')
for r in rst2:
    print(r)

print('-------------------')
rst3 = (x * x for x in range(11))
for r in rst3:
    print(r)


# 实现斐波拉契函数
print('---------实现斐波拉契函数----------')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    print 'done'
rst4 = fib(6)

#要把fib函数变成generator
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    print 'done'
g = fib_generator(6)
while True:
    try:
        x=next(g)
        print('g:', x)
    except StopIteration as s:
        print('Generator return value:' , s.value)
        break