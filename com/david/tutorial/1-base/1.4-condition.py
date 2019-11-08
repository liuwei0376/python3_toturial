#-*- coding:utf-8 -*-

'''
条件判断 if elif else
'''
print '----------例子1-----------'
flag = False
name = 'david'
if name == 'admin':
    flag = True
    print 'welcome boss'
else:
    print name

print '----------例子2-----------'
'''
根据Num值判断其所在的标签
'''
num = 5
if num == 3:
    print 'boss'
elif num == 2 :
    print 'user'
elif num == 1:
    print 'worker'
elif num <0:
    print 'error'
else :
    print 'vip'

print '----------例子3-----------'
'''
if语句包含多个条件
'''
num=9
if num > 0 and num < 10:
    print 'num > 0 and num < 10_1-spider'
elif num <0 or num >=10:
    print 'num <0 or num >=10_1-spider'
else:
    print 'undefine'

# -------
# 判断值是否在0~5或10~15之间
num = 4
if (num>=0 and num<=5) or (num>=10 and num <=15):
    print '值在0~5或10~15之间'
else:
    print '值不在此区间'

#----------
# 同一行中使用if条件判断语句
var = 100
if var == 100:print '变量var的值是100'

print "good bye"

print '----------例子4-----------'
'''
短路判断之 and 操作
'''
a1 = 0
b1 = 1
if (a1>0) and (b1/a1 > 2):
    print 'yes-1'
else:
    print 'no-1'

'''
短路判断之 or 操作,报错：
ZeroDivisionError: integer division or modulo by zero
'''
a1 = 1
b1 = 1
if (a1>0) or (b1/a1 > 2):
    print 'yes-2'
else:
    print 'no-2'

print '----------例子5-----------'
'''
简单条件循环实现汉诺塔问题
'''
# def my_print(args):
#     print args

# def move(n, a, b, c):



age = 5
if age>18:
    print('Your age is',age)
    print('Adult')
else:
    print("your age is", age)
    print('teenager')


if age>=18:
    print('Your age is', age)
    print('Adult')
elif age>=6:
    print("your age is", age)
    print('teenager')
else:
    print("your age is", age)
    print('kid')

x = '' # 0/[]/()
#x 非0、非空字符串、非空list，就判断为True，否则为False
if x:
    print('True')
else:
    print('False')

#用户手动输入
s = input('birthday:')
birth = int(s)
if birth < 1980:
    print('70后。。。')
else:
    print('80后。。。')

