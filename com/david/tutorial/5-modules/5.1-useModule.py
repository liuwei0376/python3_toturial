# -*- coding:utf-8 -*-

'My test module'

'''
!/usr/bin/env python3 #直接在Unix/Linux/Mac上运行
第四行
是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ 可以备注作者信息

sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
'''
__author__ = 'David'

import sys

def my_func():
    args = sys.argv
    print('args : %s' % args)
    print('docs : %s' % __doc__)
    if len(args) == 1:
        print('Hello,World')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments')

'''
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命
令行运行时执行一些额外的代码，最常见的就是运行测试。
'''
if __name__ == '__main__':
    my_func()
