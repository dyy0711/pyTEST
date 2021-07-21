#标准算数运算符
print(1+1)    #加法运算
print(1-1)    #减法运算
print(2*4)    #乘法运算
print(1/2)    #除法运算
print(11//2)  #整除运算  结果为5
print(11/2)   #除法运算  结果为5.5
print(11%2)   #取余运算  结果为1
print(2**3)   #幂运算，表示2的3次方 结果为8
print(9//4)
print(9//-4)  #一正一负的整数公式，向下取整
#一正一负的取余要看公式，余数=被除数-除数*商
print(9%-4)    #余数=9-（-4）*（-3）=-3
print(-9%4)    #余数=-9-4*（-3）=3

#赋值运算符
#支持链式赋值
a=b=c=30
print(a,id(a))   #id()表示标识或内存
print(b,id(b))
print(c,id(c))
#支持参数赋值
i=20
i+=30     #相当于i+30再赋值给i
print(i)   
i-=10     #相当于i-10再赋值给i
print(i)
i*=2      #相当于i*2再赋值给i
print(i)
i/=3      #相当于i/3再赋值给i
print(i)
i//=2     #相当于i//2再赋值给i
print(i)
i%=3      #相当于i%3再赋值给i
print(i)
#支持系列解包赋值
a,b,c=20,30,40     #要求=左右两端的个数相同
print(a,b,c)
#交换两个变量的值
a,b=10,20
print('交换之前a,b的值:',a,b)
a,b=b,a
print('交换之后a,b的值:',a,b)

#比较运算符 （比较运算符的结果为布尔类型）
a,b=10,20
print('a>b吗?',a>b)
print('a<b吗?',a<b)
print('a<=b吗?',a<=b)
print('a>=b吗?',a>=b)
print('a=b吗?',a==b)   
print('a!=b吗?',a!=b)
'''一个=称为赋值运算符，两个=即==称为比较运算符
一个变量由三部分组成：标识、类型、值。 ==比较的是值
比较对象的标识使用的 is'''
a=10
b=10
print(a==b)      #True 说明a与b的value相等
print(a is b)    #True 说明a与b的标识相等
#后面会讲解的代码
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)     #比较value  True
print(lst1 is lst2)   #比较id     False
print(lst1 is not lst2)