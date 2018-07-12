#-*- coding:utf-8 -*-

if True:
    print 'true'
    print 'True'
else:
    print 'false'
    print 'False'

days = ['monday',
        'tuesday','wednesday']

word = 'word'
sentense = "这是一个句子"
paragraph = """这是一个段落。
包含了多哦语句"""

# 这是一个注释

'''
多行注释
'''

"""
双引号凡是的杜航注释
"""

#raw_input('\n\nPress the entry key to exit:')

# 同一行显示多条语句
import sys; x = 'david'; sys.stdout.write(x + '\n')

x = 'a'
y = 'b'
print x
print y
# 不换行输出
print '-------------------'
print x,
print y,

print '-------------------'
age = 30
if age <15:
    print 'child'
elif age >=15 and age <=35:
    print 'youth'
else:
    print 'older'

a=b=c=1
print a,b,c
a,b,c=1,2,'david'
print a,b,c

# python中五种标准数据类型
# Numbers(数字)
# String(字符串)
# List(列表)
# Tuple（元祖）
# Dictionary（字典）
var1=1
var2=2
del var1,var2

#python中数字有4种
#int long float complex(复数)
longtype=-0x19323L
complex_type = 4.53e-7j

#字符串
s = 'ilovepython'
print s[1:5]

print '---------------------'
str = "Hello World!"
print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + "TEST"

# python 列表
list = ['liujingyang',2,'2015-07-29',376,92]
tinylist = [30, 'lige']
print list
print list[0]
print list[1:3]
print tinylist *2
print list +tinylist

#python 元组
#类似于list，内部用逗号隔开，不能二次赋值，相当于只读列表
tuple = ('liujingyang',2,'2015-07-29',376,92)
tinytuple = (30, 'lige')
print tuple
print tuple[0]
print tuple[1:3]
print tinytuple * 2
print tuple + tinytuple
print '--------------'


# 字典
#类比java hashMap，无序，通过键来存取
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'
tinydict = {'name': 'john', 'code':3344, 'dept':'it'}
print dict['one']
print dict[2]
print tinydict
print tinydict['name']
print tinydict['dept']
print tinydict.keys()
print tinydict.values()

#python数据类型转换
print int('123')
print long('4567')
print float('4567')
print complex(2,3)
# print tuple(1,2,3)
# print list(4,2,3)
print hex(1)
print 10**20
print 9//2
print 9.0//2

a = 20
b = 20

if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if (a is b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if (a is not b):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"