# -*- coding:utf-8 -*-

'''
使用元类

metaclass允许你创建类或者修改类，即，类可以看做是metaclass创建出来的实例。
类比java的 clazz
'''


class Hello(object):
    def hello(self, name='world'):
        print('hello, %s' % name)


'''
type()函数可以查看一个类型或变量的类型，class的类型就是type
'''
print(type(Hello))  # 打印<type 'type'>

'''
type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
'''
print('-------------------- 使用type() 函数创建一个类 ----------------------')


def fn(self, name='world'):
    print('hello, %s' % name)


'''
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''
Hello2 = type('Hello2', (object,), dict(hello2=fn))
h = Hello2()
h.hello2()
print(type(Hello2))  # <type 'type'>
print(type(h))  # <class '__main__.Hello2'>

#测试未通过
# # metaclass是类的模板，所以必须从`type`类型派生：
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
#
# class MyList(list, metaclass=ListMetaclass):
#     pass
#
# L = MyList()
# L.add(1)
# print(L)
