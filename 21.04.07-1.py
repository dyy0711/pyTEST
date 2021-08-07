#字符串的常用操作
'''center()函数---居中对齐'''
s='hello,Python'
print(s.center(20,'*'))     #结果为****hello,Python****
'''ljust()函数---左对齐'''
print(s.ljust(20,'*'))      #结果为hello,Python********
'''rjust()函数---右对齐'''
print(s.rjust(20,'*'))      #结果为********hello,Python
'''zfill()函数---右对齐，左侧用0填充，仅接受一个参数'''
print(s.zfill(20))          #结果为00000000hello,Python

#字符串的劈分操作
'''split()---从字符串左侧开始劈分,返回为列表
用sep指定劈分符，默认为空格
用maxsplit指定最大劈分次数'''
s='hello world Python'
lst=s.split()
print(lst)                    #结果为['hello', 'world', 'Python']
s1='hello|world|Python'
print(s1.split())             #结果为['hello|world|Python']
print(s1.split(sep='|'))      #结果为['hello', 'world', 'Python']
print(s1.split(sep='|',maxsplit=1))    #结果为['hello', 'world|Python']
'''rsplit()---从字符串右侧开始劈分,返回为列表
用sep指定劈分符，默认为空格
用maxsplit指定最大劈分次数'''
s='hello world Python'
print(s.rsplit())            #结果为['hello', 'world', 'Python']
s1='hello|world|Python'
print(s1.rsplit(sep='|'))   #结果为['hello', 'world', 'Python']
print(s1.rsplit(sep='|',maxsplit=1))    #结果为['hello|world', 'Python']

#判断字符串的方法
'''isidentifier()---判断指定的字符串是不是合法的标识符'''
s='hello,python'
print('1',s.isidentifier())      #False 合法的标识符是字母、数字、下划线
print('2','hello'.isidentifier())   #True
print('3','张三_'.isidentifier())   #True
print('4','张三_123'.isidentifier())  #True
'''isspace()---判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）'''
print('5','\t'.isspace())           # True
print('6','\n'.isspace())           # True
'''isalpha()---判断指定的字符串是否全部由字母组成'''
print('7','abc'.isalpha())          # True
print('8','张三'.isalpha())         # True
print('9','张三1'.isalpha())        # False
'''isdecimal()---判断指定的字符串是否全部由十进制的数字组成'''
print('10','123'.isdecimal())       # True
print('11','123四'.isdecimal())     # False
print('12','ⅡⅡⅡ'.isdecimal())    # False
'''isnumeric()---判断指定的字符串是否全部由数字组成'''
print('13','123'.isnumeric())      # True
print('14','123四'.isnumeric())    # True
print('15','ⅡⅡⅡ'.isnumeric())   # True
'''isalnum()---判断指定字符串是否全部由数字和字母组成'''
print('16','abc1'.isalnum())      # True
print('17','张三123'.isalnum())   # True
print('18','abc!'.isalnum())     # False   

#字符串替换
'''replace（）---字符串的替换
第一个参数指定被替换的字符串
第二个参数指定替换字符串
第三个参数指定最大替换次数'''
s='hello,Python'
print(s.replace('Python','Java'))        #结果为hello,Java
s1='hello Python Python Python'
print(s1.replace('Python','Java',2))     #结果为hello Java Java Python

#字符串的合并
'''join（）---字符串的合并
将列表或元组中的字符串合并成一个字符串'''
lst=['hello','java','Python']
print('|'.join(lst))     #结果为hello|java|Python
print(''.join(lst))      #结果为hellojavaPython
t=('hello','Java','Python')
print(''.join(t))        #结果为helloJavaPython
print('*'.join('Python'))   #结果为P*y*t*h*o*n

#字符串的比较操作
print('apple'>'app')    #True
print('apple'>'banana')  #False
print(ord('a'),ord('b'))   #ord(a)=97   ord(b)=98
print(chr(97),chr(98))
print(ord('董'))
print(ord('钟'))
'''==与is的区别
==比较的是value是否相等
is比较的是id是否相等'''

#字符串的切片操作
s='hello,Python'
s1=s[:5]               #由于没有指定起始位置，所以从0开始切
s2=s[6:]               #由于没有指定结束位置，所以一直切到结束位置
s3='!'
newstr=s1+s3+s2
print(s1)
print(s2)
print(newstr)
print('------------切片[start:end:step]---------')
print(s[1:5:1])       #从1开始截到5（不包含5），步长为1
print(s[::2])         #默从0开始，没有写结束，默认到字符串的最后一个元素，步长为2，两个元素之间的索引间隔为2
print(s[::-1])        #默认从字符串的最后一个元素开始，到字符串第一个元素结束，因为步长为负数
print(s[-6::1])       #从索引为-6开始，到字符串的最后一个元素结束，步长为1

#格式化字符串
'''第一种方式，%作占位符'''
name='张三'
age=20
print('我叫%s,今年%d岁' % (name,age))
'''第二种方式，{}作占位符'''
name='张三'
age=20
print('我叫{0}，今年{1}岁'.format(name,age))
'''第三种方式，f-string'''
name='张三'
age=20
print(f'我叫{name},今年{age}岁')
'''指定精度和宽度'''
print('%10d' % 99)          #10表示宽度
print('%f' % 3.1415926)
print('%.3f' % 3.1415926)    #保留三位小数
'''同时表示宽度和精度'''
print('%10.3f' % 3.1415926)   #总宽度为10，小数点后三位
print('{}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))     #.3表示一共是3位数
print('{0:.3f}'.format(3.1415926))    #.3f表示是3位小数
print('{0:10.3f}'.format(3.1415926))  #同时设置，精度是10，3位小数

#字符串的编码转换
s='天涯共此时'
'''编码'''
print(s.encode(encoding='GBK'))      #在GBK这种编码格中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))    #在UTF-8这种编辑格式中，一个中文占三个字节
'''解码'''
byte=s.encode(encoding='GBK')       #byte代表是一个二进制数据（字节类型的数据）
print(byte.decode(encoding='GBK'))
byte1=s.encode(encoding='UTF-8')
print(byte1.decode(encoding='UTF-8'))