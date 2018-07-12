# -*- coding:utf-8 -*-

# python除了正常定义的必选参数外，还可以使用默认参数/可变参数和关键字参数，
# 使得定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 1.位置参数
def power(x):
    return x * x


print(power(5))


# 计算x的n次方
def power(x, n):
    rst = 1
    while (n > 0):
        rst = rst * x;
        n = n - 1
    return rst


print(power(5, 1))
print(power(5, 2))
print(power(5, 4))


# 2。默认参数
# 默认情况下，power一般是指平方的计算，所以可以在上一个函数的基础上，给第二个参数指定一个默认参数
def diypower(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(diypower(5))
print(diypower(5, 3))

'''
总结：
设置默认参数是，要注意：
1。必选参数在前，默认参数在后
2.函数有多个参数时，把变化大的参数放前面，变化小的放后面，变化小的作为摩恩参数
3.默认参数必须指向不可变对象
'''
def enroll(name,gender,city='Shanghai',age=3):
    print("Below is function enroll's input parameters")
    print("name:\t",name)
    print("gender:\t",gender)
    print("city:\t",city)
    print("age:\t",age)
    print("-----------")

print(enroll('liujingyang','m'))
print(enroll('pipi','m','haikou',5))
print(enroll('john','m',age=2))

def add_end(L=[]):
    L.append("END")
    return L
print(add_end([1,2,3]))

'''
如下3项，将返回3种结果
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''
print(add_end())
print(add_end())
print(add_end())

#定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end2(L=None):
    if L is None:
        L=[]
    L.append("END")
    return L
print(add_end2())
print(add_end2())
print(add_end2())

# 计算a*a + b*b + c*c + 。。。 + n*n
#方式一。
#这种方式定义函数，需要传入list或tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum
print(calc([1,2,3]))
print(calc((1,2,3)))

#方法二.这样设计传递的参数可以不必是list或tuple
def calc_params_can_change(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum
print(calc_params_can_change(1,2,3))
print(calc_params_can_change(1,2,3,4))

num=[1,2,3,4,5]
num2=(1,2,3,4,5)
print(calc_params_can_change(num[0],num[1],num[2],num[3],num[4]))
print(calc_params_can_change(num2[0],num2[1],num2[2],num2[3],num2[4]))
'''如果已经有一个list或tuple，可以
在参数前加*号，把list或tuple的元素变成可变参数
传递进去'''
print(calc_params_can_change(*num2))

#3.关键字参数
def person(name,age,**kw):
    print('name:',name,',age:',age,',other:',kw)

person('david','77')
person('dove','23',city='Shanghai')
person('smith','36',gender='M',job='pythonProgrammer')

extra={'city':'bj','job':'javaprogrammer'}
#**extra表示将extra这个dict的key-value用关键字参数传入
#到**kw中，kw获取到的是dict字典
person('Zhangsan',22,**extra)
