#函数的创建
def calc(a,b):     #a,b称为形式参数，简称为形参，形参的位置是函数的定义处
    c=a+b
    return(c)
result=calc(10,20)   #10，20称为实际参数的值，简称为实参，实参的位置是函数的调用处
print(result)
res=calc(b=10,a=20)  #=左侧的变量的名称称为关键字参数
print(res)
'''在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响到实参的值
如果是可变对象，在函数体的修改会影响到实参的值'''
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)
print('n1',n1)       #arg1的修改为100，不会影响n1的值
print('n2',n2)       #arg2的修改，append(10)，会影响到n2的值

#函数返回值
'''函数返回多个值时，结果为元组'''
def fun(num):
    odd=[]      #存奇数
    even=[]     #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
print(fun([10,29,34,23,44,53,55]))
'''
函数的返回值
（1）如果函数每日有返回值【函数执行完毕之后，不需要给调用处提供数据】 return可以省略不写
（2）函数的返回值，如果是1个，直接返回原类型
（3）函数的返回值，如果是多个，返回的结果为元组
'''
'''返回值第一种情况'''
def fun1():
    print('hello')
fun1()
'''返回值第二种情况'''
def fun2():
    return 'hello'
res=fun2()
print(res)
'''返回值第三种情况'''
def fun3():
    return 'hello','world'
res1=fun3()
print(res1)                   #'''函数在定义时，是否需要返回值，视情况而定'''

#函数的参数定义
'''函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参'''
def fun(a,b=10):    #b为默认值参数
    print(a,b)
fun(100)
fun(20,30)

def fun(*args):
    print(args)
fun(10)
fun(10,30)
fun(30,405,50)

def fun1(**args):
    print(args)
fun1(a=10)
fun1(a=20,b=30,c=40)

'''def fun(*arg,*a):
   pass
    以上代码程序会报错，个数可变的位置参数，只能是1个
def fun2(**args,**args):
    pass
    以上代码程序会报错，个数可变的关键字参数，只能是1个
'''
def fun2(*args1,**args2):
    pass

'''def fun3(**args1,*args2):
    pass
   在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求个数可变的位置形参，放在个数可变的关键字形参之前
'''

def fun(a,b,c):#a,b,c在函数的定义处，所以是形式参数
    print('a=',a)
    print('b=',b)
    print('c=',c)
fun(10,20,30)  #函数调用时的参数传递，称为位置传参
lst=[11,22,33]
fun(*lst)   #在函数调用时，将列表中的每个元素都转换为实参传入
fun(a=100,c=300,b=200)    #函数的调用，所以是关键字实参
dic={'a':111,'b':222,'c':333}
fun(**dic)       #在函数调用时，将字典中的键值对都转换成关键字实参传入
 
def fun(a,b=10):    #b是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=',a)
    print('b=',b)

def fun2(*args):   #个数可变的位置形参
    print(args)
def fun3(**args2):
    print(args2)    #个数可变的关键字形参
fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44,e=55)

def fun4(a,b,*,c,d):   #从*之后的参数，在函数调用时，只能采用关键字参数传递。表示c,d只能采用关键字传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
#fun4(10,20,30,40)   #位置实参传递
fun4(a=10,b=20,c=30,d=40)  #关键字实参传递
fun4(10,20,c=30,d=40)     #前两个参数，采用的是位置实参传递，而c,d采用的是关键字实参传递
'''函数定义时的形参的顺序问题'''
def fun5(a,b,*,c,d,**args2):
    pass
def fun6(*args,**arges):
    pass
def fun7(a,b=10,*args,**args2):
    pass

#变量
def fun(a,b):
    c=a+b        #c,就称为局部变量，因为c在函数体内进行定义的变量，a,b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)
#print(c)   程序报错，因为a,c超出了起作用的范围（超出了作用域）
name='杨老师'       #name的作用范围为函数内部和外部都可以使用---称为全局变量
def fun2():
    print(name)
fun2()

def fun3():
    global age    #函数内部定义的变量，局部变量，局部变量使用global声明，这个变量实际上就变成了全局变量
    age=20
    print(age)
fun3()
print(age)

#递归函数
'''利用递归函数，计算阶乘'''
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))

#斐波那契数列----1，1，2，3，5，8，13.。。。。。。
'''利用递推求斐波那契数列的第n项'''
def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)
print(fun(6))
print('-----斐波那契数列的前六项------- ')
for i in range(1,7):
    print(fun(i),end=' ')