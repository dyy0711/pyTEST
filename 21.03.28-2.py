#不可变序列，可变序列
'''可变序列：列表，字典'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))     #增加数字前后列表的id没有变 说明列表可以增加
'''不可变序列：字符串，元组'''
s='hello'
print(id(s))
s=s+'world'
print(s)
print(id(s))    #虽然能增加，但id发生变化，已经不是原来的字符串了

#元组的创建方式
'''第一种，直接小括号'''
t=('Python','world',90)
print(t,type(t))
t2='Python','world',91   #直接使用小括号的表示方法，小括号可以不写
print(t2,type(t2))
'''第二种，使用内置函数tuple（）'''
t1=tuple(('Python','world',93))
print(t1,type(t1))
'''第三种，只包含一个元组的元素需要使用逗号和小括号'''
t3=('Python',)
print(t3)
'''空元组的创建方式'''
t4=()
t5=tuple()

#元组的遍历
t=('Python','world',98)
'''第一种获取元组的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
'''遍历元组'''
print('遍历元组')
for item in t:
    print(item)