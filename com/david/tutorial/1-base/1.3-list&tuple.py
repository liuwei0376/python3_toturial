#-*- coding:utf-8 -*-

### 使用list和tuple

#LIST 列表
#python内置的数据类型，是一种有序的集合，可以随时add或delete元素
classmates = ['Michael','Lily','Lucy']
print( classmates)
print( len(classmates))
#使用索引来访问list元素
print(classmates[0])
print(classmates[1])
print(classmates[2])
#获取list最后一个元素
print(classmates[-1])

#最佳元素到list中
classmates.append('Hanmeimei')
print(classmates)

#把元素追加到指定的位置
classmates.insert(1,'david')
print(classmates)

#删除末尾元素
classmates.pop()
print(classmates)

#删除指定位置的元素
classmates.pop(1)
print(classmates)

#list里元素类型可不必相同
A = ['apple', 123, False]

#list嵌套
Embed = ['java','python',['jsp','asp','php'],'C++']
print(len(Embed))

a = ['jsp','asp','php']
b = ['java','python',a,'C++']
print(b)
print(b[2][2]) #拿php 二维数组


#Tuple 列表
#另一种有序列表叫元组，tuple和list类型，但tuple一旦初始化就不能修改。
print("\n\n如下为Tuple测试\n\n")
classmates2 = ('Michael','Lily','Lucy')
print(classmates2)
print(classmates2[0])
print(classmates2[1])
print(classmates2[2])
print(classmates2[-1]) #打印最后一个元素

t = (1,2)
t = ()

#定义一个只有一个元素的陷阱
t = (1)
print(t)
#只有一个元素的tuple，定义时，必须要在元素后面加一个逗号“,”，以消除歧义
t = (1,)
print(t)

#可变tuple
t = ('h5','ios',['huawei','sumsang'])
print(t)
t[2][0] = "xiaomi"
t[2][1] = 'vivo'
print(t)


