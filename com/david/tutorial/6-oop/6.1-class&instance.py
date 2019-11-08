# -*- coding:utf-8 -*-

'''
面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。

所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。

面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

小结
数据封装、继承和多态是面向对象的三大特点

小结
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

'''

class Student(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def print_address(self):
        print("name:%s, address:%s" % (self.name,self.address))

    def print_district(self):
        if self.address == 'shanghai':
            return 'HuaDong'
        elif self.address == 'shenzhen':
            return 'HuaNan'

stu1 = Student('david','shanghai')
stu2 = Student('lijian','shenzhen')

stu1.print_address()
stu2.print_address()
print(stu1.name,stu1.address,stu1.print_district())
print(stu2.name,stu2.address,stu2.print_district())
