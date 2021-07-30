lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
#列表
'''创建列表的第一种方式，使用[]'''
lst=['hello','world',98]
'''创建列表的第二种方式，使用内置函数list()'''
lst2=list(['hello','world',98])

#列表的索引
lst=['hello','world',98,'hello']
print(lst.index('hello'))  #如果列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
print(lst.index('hello',1,4))  #在指定的范围内查找元素的索引
#获取列表中的单个元素
lst=['hello','world',98,'hello','world',234]
print(lst[2])   #获取索引为2的元素
print(lst[-3])  #获取索引为-3的元素
#获取列表中的多个元素
'''步长为正数的情况'''
lst=[10,20,30,40,50,60,70,80]
print(lst[1:6:1])    #start=1 stop=6 step=1  start不写默认为0，stop不写默认为最后，step不写默认为1
'''步长为负数的情况'''
print(lst[::-1])   #结果为原列表的逆序
#判断指定元素在列表中是否存在
'''使用in   not in'''
lst=[10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)
'''列表元素的遍历'''
print('--------------------')
for item in lst:
    print(item)
#列表元素的增加
'''append()--在列表的末尾添加一个元素'''
lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))   #标识相同，没有创建新列表
'''extend()--在列表的末尾至少添加一个元素'''
lst2=['hello','world']
#lst.append(lst2)   #将lst2作为一个元素添加到lst中
print(lst)   
lst.extend(lst2)    #将lst中的每一个元素分别添加到lst列表的末尾
print(lst)
'''insert()--在列表的任意位置添加一个元素'''
lst.insert(1,90)
print(lst)
'''切片---在列表的任意位置添加至少一个元素'''
lst3=[True,False,'hello']
lst[1:]=lst3
print(lst)

#列表元素的删除
'''remove()
一次删除一个元素
重复元素只删除第一个
元素不存在抛出 ValueError'''
lst=[10,20,30,40,50,60,30]
lst.remove(30) 
print(lst)
'''pop()
删除一个指定索引位置的元素
指定索引不存在抛出IndexError
不指定索引则删除列表中的最后一个元素'''
lst=[10,20,30,40,50,10]
lst.pop(1)
print(lst)   #指定索引
lst.pop()
print(lst)   #不指定索引
'''切片---一次至少删除一个元素'''
lst=[10,20,30,40,50]
lst1=lst[1:3]
print('原列表',lst)
print('切片后列表',lst1)   #产生新列表对象的切片
lst[1:3]=[]
print(lst)        #不产生新的列表对象，二十删除原列表中的内容
'''clear()---清空列表'''
lst.clear()
print(lst)
'''del---删除列表'''
#lst.del   #lst列表被删除 在输出lst列表时，程序会报错

#列表元素的修改
'''为指定索引的元素赋予一个新值'''
lst=[10,20,30,40,50]
lst[2]=100
print(lst)
'''为指定的切片赋予一个新值'''
lst[1:3]=[0,0]
print(lst)

#列表元素的排序操作
'''第一种，调用sort（）方法，
列表中的所有元素默认按照从小到大的顺序进行排序，
可以指定reverse=True，进行降序排序'''
lst=[10,0,30,45,63,57,33]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
'''第二种，调用内置函数sorted(),
可以指定reverse=True，进行降序排序
原列表不发生改变'''
lst=[10,0,30,100,45,63,57,33]
lst1=sorted(lst)
print(lst1)
lst2=sorted(lst,reverse=True)
print(lst2)

#列表生成式
lst=[i for i in range(1,10)]
print(lst)
'''列表中的元素的值为2，4，6，8，10'''
lst=[i for i in range(2,11,2)]
print(lst)