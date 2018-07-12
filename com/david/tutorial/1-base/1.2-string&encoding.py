#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#python3中，字符串是以Unicode编码的，即python字符串支持多语言
print('包含中文的string')

#ord获取字符的整数表示、chr把编码转化为对应的字符
print(ord('A'))
print(chr(65))

print('\u4e2d\u6587')

#如果需要保存到磁盘行，或需要在网络层传输，需要保存为以字节为单位的bytes
x=b'ABC'
print(x)

print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))

#字符串格式化
print('Hi, %s, you have %d $.' % ('david', 10000))
print("HI, {0}, 你又长高了 {1:.2f} 厘米".format('刘旌扬',10.275))


