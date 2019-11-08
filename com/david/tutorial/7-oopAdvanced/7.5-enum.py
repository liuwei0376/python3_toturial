#-*- coding:utf-8 -*-

'''
Python中的枚举
'''
from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

#可以直接用Month.Jan引用引用一个变量，变量值为int性，从1开始
for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


#如果需要更精准的控制枚举类型，可以从Enum中派生出自定义类：
from enum import Enum,unique

class Weekday(Enum):
    Sunday = 0 #自定义sunday的值为0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

day1 = Weekday.Monday
print('day1: %s' % day1)
print(Weekday.Tuesday)
print(Weekday['Saturday'])
print(Weekday.Saturday.value)
print(day1 == Weekday.Monday)
print(day1 == Weekday.Tuesday)
print(Weekday(1))
# print(Weekday(7)) #ValueError: 7 is not a valid Weekday

'''
总结：既可以用成员名称引用枚举变量，也可以直接根据value只来获得枚举变量
'''

#联系，把student类的gender改造为枚举类型
from enum import Enum
class Gender(Enum):
    Male = 1
    Female = 2
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

#测试
stud1 = Student('zhangsan',Gender.Male)
if stud1.gender == Gender.Female:
    print('测试通过')
else:
    print('测试失败')