#-*- coding:utf-8 -*-

#转义
stateent='I\'m \"OK\" !'
print(stateent)
print('I\'m learning\npython.')
print('\\\t\\')
#r表示默认不转义
print(r'\\\t\\')

#储存多行内容
print("""
I'm line1;
I'm line2;
""")

#布尔值
print(3>2) #True
print(3<2) #False

#与、或、非
print(True and False)
print(True or False)
print(not False)

#空值
print(None)

#变量
a=1
t_007='t007'
Answer=True
Answer=123 #变量类型本身不固定，则python为动态语言，而java为静态语言。

#常量,PYTHON中用大些的变量表示常量
PI=3.1415926