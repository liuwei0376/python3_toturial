#-*- coding:utf-8 -*-

'''
StringIO顾名思义就是在内存中读写str
'''

from io import StringIO as StringIO
from io import BytesIO as StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

'''
要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
'''
from io import StringIO as StringIO
from io import BytesIO as StringIO
f2 = StringIO('Hello\nHi\nGood')
while True:
    line = f2.readline()
    if line == '':
        break
    print(line.strip())


# from io import BytesIO
# f3 = BytesIO()
# f3.write('中文'.encode('utf-8'))
# print(f3.getvalue())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())