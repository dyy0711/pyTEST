#字符串
#字符串的驻留机制
a='Python'
b="Python"
c='''Python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))

#字符串的查询操作
'''index()
查询子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError'''
s='hello,hello'
print(s.index('lo'))   #结果为3
'''rindex()
查找子串substr最后一次出现的位置，如果查找的子串不存在，则抛出ValueError'''
print(s.rindex('lo'))  #结果为9
'''find()
查找子串substr第一次出现的位置，如果查找子串不存在时，则返回-1'''
print(s.find('lo'))  #结果过是3
'''rfind()
查找子串substr最后一次出现的位置，如果查找子串不存在时，则返回-1'''
print(s.rfind('lo'))   #结果为9

#字符串的大小写转换操作
s='hello,python'
'''upper()
把字符串中所有字符都转成大写字母'''
s1=s.upper()      #转成大写之后会变成一个新的字符串对象
print(s1)
'''lower()
把字符串中所有字符都转成小写字母'''
s2=s1.lower()
print(s2)
'''swapcase()
把字符串中所有大写字母转成小写字母，把所有小写字母都转成大写字母'''
a='hello,Python'
a1=a.swapcase()
print(a1)
'''capitalize()
把第一个字符转换为大写，把其余字符转换为小写'''
a2=a.capitalize()
print(a2)
'''title()
把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写'''
a3=a.title()
print(a3)