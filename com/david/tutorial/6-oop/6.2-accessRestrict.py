#-*- coding:utf-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))

    #getter方法
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    #setter方法
    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('Wrong score format')

stu1 = Student('david',22)
# print(stu1.__name) 将报错
stu1.print_score()
print(stu1.get_name())
print(stu1.get_score())
stu1.set_name('John')
print('after modify stu1 name, name is: %s' % stu1.get_name())

stu1.set_score(100)
print('after modify stu1 score, score is: %d' % stu1.get_score())

# stu1.set_score(101)
# print('after give stu1 a wrong score, score is: %d' % stu1.get_score())

stu1.__name='New name'