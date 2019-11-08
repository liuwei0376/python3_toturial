#-*- coding:utf-8 -*-

'''
一、获取对象信息
'''
print('-----------------一、获取对象信息------------------')
# 1.1 使用type()获取对象的类型
print('-----------------1.使用type()获取对象的类型------------------')

print(type(123))
print(type('str'))
print(type(None))

#如果一个变量指向函数或者类，也可以用type()判断
print(type(abs))

class Animal(object):
    def run(self):
        print('Animal is running...')

a = Animal()
print(type(a))

#type()函数返回的是Class类型，如需要比较2个变量的type类型是否相同：
print(type(123)==type(456))
print(type(0376)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))

#判断基本类型可以直接写int，str等，如果要判断一个对象是否是函数怎么办？
print('-----------------判断基本类型可以直接写int，str等，如果要判断一个对象是否是函数怎么办？------------------')
import types

def my_fn():
    pass

print(type(my_fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x*x)==types.LambdaType)
print(type(x for x in (1,10)) == types.GeneratorType)

'''
二、使用isinstance()
'''
print('-----------------使用isinstance()------------------')

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eat bone')


class Husky(Dog):
    def run(self):
        print('Husky is running...')
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))

print(isinstance(d,Dog) and isinstance(d,Animal))
print(isinstance(d,Husky))

print('-----------------能用type判断的基本类型也可以用isinstance()判断------------------')
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

print('-----------------还可以判断一个变量是否为某些类型中的一种------------------')
print(isinstance([1,2,3],(list, tuple)))
print(isinstance((1,2,3),(list, tuple)))

'''
三、获取对象信息
'''
print('-----------------三、获取对象信息------------------')

#如果要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含
#字符串的list，比如获取一个str的所有属性和方法
print(dir('abc'))

#len()内部 ，自动调用该对象的__len__方法，以下代码等价：
print(len('abc'))
print('abc'.__len__())

#自己写的类，如果也想用len(myObj)的话，就重写__len__()方法：
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))
print(len('abcde'))

print('-----------------配合getattr()/setattr()/hasattr()，'
      '可以直接操作一个对象的状态------------------')
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print('hasattr(obj,\'x\'): %s' % hasattr(obj,'x'))
print('obj.x ： %s' % obj.x)
print('hasattr(obj,\'y\'): %s' % hasattr(obj,'y'))
setattr(obj,'y',20)
print('hasattr(obj,\'y\'): %s' % hasattr(obj,'y'))
print('obj.y ： %s' % obj.y)
print('getattr(obj,\'y\'): %s' % getattr(obj,'y'))

#可以传入一个default参数，如果属性不存在，则返回默认值
print(getattr(obj,'z',404))


print('-----------------获取对象的方法------------------')
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
#获取属性'power'并赋值到变量fn
fn = getattr(obj,'power')
print(fn)
#调用fn与调用obj.power()是一样的
print(fn())