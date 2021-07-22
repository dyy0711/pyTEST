# 布尔运算符
# and(并且)
a,b=1,2
print(a==1 and b==2)   # True and True=True
print(a==1 and b<2)    # True and False=False
print(a!=1 and b==2)   # False and True=False
print(a!=1 and b!=2)   # False and False=False
# or(或者)
print(a==1 or b==2)    # True or True=True
print(a==1 or b<2)     # True or False=True
print(a!=1 or b==2)    # False or True=True
print(a!=1 and b!=2)   # False or False=False
# not(非--对布尔类型的操作数取反)
f=True
f2=False
print(not f2)
# in与not in
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
# 位运算符
print(4&8)     #按位与&，同为1时结果为1，否则为0
print(4|8)     #按位或|，同为0时结果为0，否则为1
print(4<<1)    #左移位，高位溢出，低位补零，相当于乘以2
print(4>>1)    #右移位，低位溢出，高位补零，相当于除以2
# 运算符的优先级
# 算数运算符--位运算符--比较运算符--布尔运算符--赋值运算符