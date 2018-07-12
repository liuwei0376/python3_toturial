#-*- coding:utf-8 -*-

##循环
# 1. for x in ... 循环是把每个元素代入变量x，然后执行缩进块的语句
names = ['David','Lily','Lucy']
for n in names:
    print(n)

# 例子：计算 1+2+3。。。。+10
sum1 = 0
for n in (1,2,3,4,5,6,7,8,9,10):
    sum1 += n
print('sum1 is: ',sum1)

sum2 = 0
for n in [1,2,3,4,5,6,7,8,9,10]:
    sum2 += n
print('sum1 is: ',sum2)

print(list(range(1,101,1)))
sum3 = 0
for n in list(range(1,101,1)):
    sum3 += n
print('sum3 is: ',sum3)


# 2. 使用while循环
num=99;sum4=0
while num>0:
    sum4+=num
    num = num -2
    print('num=',num,', sum4=',sum4)
    print'num=',num,', sum4=',sum4
print('sum4 = ',sum4)

# 3. break 语句可以直接退出循环，contine可以提前结束本轮循环，并直接开始下一轮循环。
# 这两个都必须配合if语句使用
n = 0
while n<10:
    n+=1
    if n> 3:
        break;
    print(n)

n = 0
while n<10:
    n+=1
    if n%2 == 0:
        continue;
    print(n)
