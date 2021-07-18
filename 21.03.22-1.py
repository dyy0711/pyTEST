#将数据输出文件中
fp=open('D:/text.txt','a+')     #a+如果文件不存在就创建，存在就在文件的内容后面继续追加
print('helloword',file=fp)      #注意点：1.所指定的盘符存在   2.使用file=fp
fp.close()

#不进行换行输出（将输出内容写在一行中）
print('hello','world','python')

#转义字符
print('hello\nworld')     #\n表示换行
print('hello\tworld')     #\t表示制表，四个字符为一个制表位
print('helloooo\tworld')
print('hello\bworld')     #\b表示退格
print('hello\rworld')     #\r表示覆盖
print('hello\rword')
print('http:\\\\www.cn.com')   #两个斜线输出时仅有一个
print('老师说：\'大家好\'')     #作为输出内容而不是结束字符的'前要加入\ 双引号同理

#原字符 （不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或者R
print(r'hello\nworld\\')      #注意点：最后一个字符不能是反斜杠，但可以是两个反斜杠

#整数类型数据（可以是正数、负数、0）
n1=90
n2=-76
n3=0
print(n1,type(n1))    #type(n1)表示输出n1的数据类型
print(n2,type(n2))
print(n3,type(n3))
#整数可以表示为二进制、八进制、十进制、十进制
print('十进制',118)
print('二进制',0b10101111)
print('八进制',0o176)
print('十六进制',0x1EAF)

#浮点类型数据
a=3.14159
print(a,type(a))
b=1.1
c=2.2
d=2.1
print(b+d)
print(b+c)  #使用浮点数进行计算，可能出现小数位数不确定的情况,但只是个别情况，并非所有
#解决浮点数计算出现小数位数不确定情况的方案：引入Decimal模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型数据（True表示真为1，False表示假为0，布尔值可以转换为整数）
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
#布尔值可以转成整数计算
print(f1+1)     #2   1+1结果为2 故True表示1
print(f2+1)     #1   0+1结果为1 故False表示0

#字符串类型数据（字符串又称为不可变的字符序列，可以使用单引号、双引号、三引号来定义）
str1='人生苦短，我用python'
print(str1,type(str1))
str2="人生苦短，我用python"
print(str2,type(str2))
str3='''人生苦短，
我用python'''
print(str3,type(str3))
str4="""人生苦短，
我用python"""
print(str4,type(str4))    #单引号双引号只能写在一行，三引号可以写在两行