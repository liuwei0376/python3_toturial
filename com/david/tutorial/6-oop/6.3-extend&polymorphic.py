# -*- coding:utf-8 -*-

'''
继承和多态
'''


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eat bone')


class Cat(Animal):
    def run(self):
        print('cat is running...')


'''
当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
'''
dog = Dog()
dog.run()

cat = Cat()
cat.run()

'''
判断一个变量是否是某个类型可以用isinstanceof()来判断
'''
a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(isinstance(b,Dog))

print(type(Animal()))

'''
动态预研的‘鸭子类型’，不一定需要传入Animal类型，只要保证传入的对象有一个run方法就可以了
并不要求严格的继承关系，一个对象只要'看起来像鸭子，走起路来像鸭子'，则可以看成是鸭子。

Python的'file-like object'就是一种鸭子类型。
'''
class Timer(object):
    def run(self):
        print('start....')
