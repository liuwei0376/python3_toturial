#-*- coding:utf-8 -*-

# 1. 调用函数
print(abs(100))
print(abs(-101))
print(abs(22.33))
#TypeError
#print(abs(1,2))

print(max(3,5))
print(max(9,3,5,-1,10,88))

# 2. 数据类型转换
print(int('123'))
print(int(12.34))
print(float('23.45'))
print(str('abc123'))
print(bool(1)) #True
print(bool(''))

#函数名其实是指向一个函数的引用
a = abs
print(a(-222))

#练习，使用python内容的hex（）函数，把一个
#整数转换为十六进制
n1 = 8888
myhex = hex(n1)
print("转换后的数据为：",myhex)