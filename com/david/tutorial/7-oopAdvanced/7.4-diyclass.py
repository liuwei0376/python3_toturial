#-*- coding:utf-8 -*-

'''
定制类

除了__slots__和__len__
python的class中有很多这样有特殊用途的函数，可以帮助我们定制类
'''
class Student(object):
    def __init__(self,name):
        self.name = name

print(Student('zhangsan')) #打印出的内容为<__main__.Student object at 0x000000000222CC88>，非常不直观

#####
##### 为student类添加一个__str__()，返回一个规范的字符串
########################################################
class Student2(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object(name : %s)' % self.name
    __repr__ = __str__ # __repr__为调试服务

print(Student2('lisi')) #打印出 "Student name is lisi"

#####
##### __iter__，一个类向要被用于for ... in循环，类似list或tuple，就必须实现一个__iter()__方法，
##### 该方法返回一个迭代对象，而后，python的for循环就会不断的调用该迭代对象的__next__()方法拿到下一个
##### 值，知道遇到StopIteration错误时推出循环
#####
##### 范例：__iter()__实现斐波那契函数,实测该范例会报错
########################################################
# class Fib(object):
#     def __init__(self):
#         # 初始化两个计数器a，b
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         # 实例本身就是迭代对象，故返回自己
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
#
# for x in Fib():
#     print(x)


##### 要表现的像list那样按照下标取出元素，需要实现__getitem__()方法
########################################################
class Fib(object):
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a,b = b,a+b
        return a

f=Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[5])
