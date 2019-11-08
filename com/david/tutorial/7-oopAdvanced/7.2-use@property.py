#-*- coding:utf-8 -*-

class Student(object):
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('Value must between 0 and 100!')
        self._score = value

s = Student()
s.set_score(78)
print(s.get_score())
# s.set_score('101')
# s.set_score(101)


'''
但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
'''
class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('Value must between 0 and 100!')
        self._score = value

#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
stu = Student2()
stu.score = 60
print(stu.score)

# stu.score = 9999

'''
注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
'''
class Student3(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    def age(self):
        return 2018 - self._birth

stud3 = Student3()
stud3.birth = 1985
print(stud3.birth)
print(stud3.age())

'''
上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

小结

@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
'''