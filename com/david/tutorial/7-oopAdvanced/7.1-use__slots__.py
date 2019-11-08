# -*- coding:utf-8 -*-

class Student(object):
    pass


s = Student()
s.name = 'zhangsan'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(30)  # 调用实例方法
print(s.age)  # 测试结果

# 给实例s绑定的方法，对另一个实例是不起作用的
s2 = Student()


# s2.set_age(33)
# print(s2.age)

# 为了给所有实例都绑定方法，可以给class绑定方法
class Student(object):
    def set_addr(self, addr):
        self.addr = addr


s1 = Student()
s2 = Student()
s1.set_addr('shanghai')
s2.set_addr('beijing')
print(s1.addr)
print(s2.addr)

'''
使用__slots__

如果想要限制实例的属性，如，至允许对Student的实例添加name和age属性。
'''


class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'wangwu'
s.age = 38

# AttributeError: 'Student' object has no attribute 'addr'
#s.addr = 'guangzhou'

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.addr = 'guangzhou'
print(g.addr)


