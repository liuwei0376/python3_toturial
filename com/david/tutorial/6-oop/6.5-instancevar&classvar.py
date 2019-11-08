#-*- coding:utf-8 -*-

'''
实例属性和类属性
'''

'''
一、实例属性
二、类属性
'''
class Student(object):
    def __init__(self,name):
        self.name = name
s = Student('zhangsan')
s.score = 90
print((s.name,s.score))

class Student(object):
    name = "Student"

s = Student()#创建实例s
print(s.name) #因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)
s.name = 'lisi'
print(s.name) #由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)#但是类的属性并未消失
del s.name # 如果删除实例的name属性
print(s.name) #再次调用s.name,由于实例的name属性已删掉，类的name属性就显示出来了
