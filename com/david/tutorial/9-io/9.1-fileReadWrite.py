#-*- coding:utf-8 -*-

'''
文件读写
'''


# 一、读文件
# 要以读文件的模式打开一个文件对象，使用python内会的open()函数。
# 传入参数为：
#   1：文件名
#   2：标识符（r:读，w:写）

#由于文件读写可能产生IOError错误，一旦出错，f.close()就不会调用，这里使用finally保证
#文件读写是否出错，都能正确的关闭文件
try:
    f = open('D:\\test\\bdcTest\\bdcTraceBackend\config\producer.properties','r')
    content = f.read()
    print(content)
finally:
    if f:
        f.close()

print('-------------------------with语句语法----------------------------')
#但每次这样写，台麻烦，python中，引入with语句来自动帮我们调用close()方法
with open('D:\\test\\bdcTest\\bdcTraceBackend\config\producer.properties','r') as f:
    print(f.read())

print('\n-------------------------文件读取总结：----------------------------')
'''
文件读取总结：
1-read() ： 一次性读取全部文件，如果文件1T，可能内存直接撑爆
2-read(size) ： 每次最多读取size个字节的内容
3-readline ： 每次读取一行内容
4-readlines 一次性读取所有内容并返回一个list

故，适用的场景如下：
a)。文件很小，read()一次性读取；
b)。不确定大小，read(size)
c)。配置文件，readlines()最好用
'''
f=open('D:\\test\\bdcTest\\bdcTraceBackend\config\producer.properties','r')
for line in f.readlines():
    print(line)