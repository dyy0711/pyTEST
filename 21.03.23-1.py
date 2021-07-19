#数据类型转换
name='张三'
age=20
print(type(name),type(age))        #说明name和age的数据类型不相同
# print('我叫'+name+'今年'+age)    #当将str类型与int类型进行连接时，报错，解决方案，类型转化
print('我叫'+name+'今年,'+str(age)+'岁')      #将int类型通过str()函数转换成了str类型
#str()将其他类型转换成str类型
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
#int()将其他的类型转int类型
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))   #将str转成int类型，但前提为字符串为数字串
print(int(f1),type(int(f1)))   #float转成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2)))  将str转成int类型报错，因为字符串为小数串
print(int(ff),type(int(ff)))
#print(int(s3),type(s3))       将str转成int类型时，字符串必须为数字串（整数），非数字串是不允许转换的，会报错
#float()函数，将其他类型转成float类型
a1='128.98'
s2='76'
ff=True
a3='hello'
i=98
print(type(a1),type(s2),type(ff),type(a3))
print(float(a1),type(float(a1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(a3),type(float(a3)))     字符串中的数据如果是非字符串，则不允许转换
print(float(i),type(i))

#输入函数input()
present=input('大圣想要什么礼物呢?')
print(present)
print(present,type(present))
#练习：从键盘录入两个整数，计算两个整数的和
a=input('请输入一个加数a：')
b=input('请输入另一个加数b：')
print(int(a)+int(b))