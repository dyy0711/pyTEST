#内置函数range()的三种创建方式
'''第一种创建方式，只有一个参数（小括号里只给了一个数）'''
r=range(10)   #默认从零开始，步长为1
print(r)       #range(0,10)
print(list(r)) #用于查看range对象中的整数序列
'''第二种创建方式，给了两个参数（小括号里给了两个数）'''
r=range(1,10)    #指定了从1开始到10结束，不包括10，默认步长为1
print(list(r))
'''第三种创建方式，给了三个参数（小括号里给了三个数）'''
r=range(1,10,2)
print(list(r))  #从1开始到10结束 步长为2
'''判断指定的整数，在序列中是否存在'''
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)

#循环结构
#while循环
'''if 是判断一次，条件为True执行一次
   while是判断N+1次，条件为True执行N次'''
a=1
while a<10:
    print(a)
    a+=1   
'''0到4之间的累加和'''
print('0到4之间的累加和')
b=0
sum=0
while b<5:
    sum=sum+b
    b+=1
print(sum)
'''
四步循环法
1.初始化变量
2.条件判断
3.条件执行体（循环体）
4.改变变量
'''
'''计算1-100之间的偶数和'''
print('计算1-100之间的偶数和')
n=1
sum=0
while n<=100:
    if n%2==0:
        sum+=n
    n+=1
print('和为：',sum)
#for-in循环
for item in 'Python':  #依次从Python中取出字母赋给item
    print(item)
#range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)
#如果在循环体中不需要使用自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('人生苦短，我用Python')
'''利用for循环计算1-100的偶数和'''
sum=0
for i in range(1,101):
    if(i%2==0):
        sum+=i
print('1-100的偶数和为：', sum)
'''输出100-999之间的水仙花数'''
'''水仙花数：该数的每一位的三次方的和与这个数相等'''
sum=0
for n in range(100,1000):
   a=n//100 #得到百位
   b=n%100//10  #得到十位
   c=n%10       #得到个位
   if(n==a**3+b**3+c**3):
       print(n)
       sum+=n
print(sum)