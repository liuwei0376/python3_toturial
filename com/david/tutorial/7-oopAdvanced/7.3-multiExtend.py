#-*- coding:utf-8 -*-

'''
多重继承
'''

class Animal(object):
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixin(object):
    def run(self):
        print('Running...')

class FlyableMixin(object):
    def fly(self):
        print('Flying...')

#肉食性动物
class CarnivorousMixin(object):
    def eat(self):
        print('Eating carnivorous')
#植食性动物
class HerbivoresMixin(object):
    def eat(self):
        print('Eating herbivores')

#各种动物
class Dog(Mammal,RunnableMixin,CarnivorousMixin):
    pass

class Bat(Mammal,FlyableMixin):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


