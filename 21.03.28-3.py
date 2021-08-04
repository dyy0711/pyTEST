#集合的创建方式
'''第一种直接创建方式'''
s={2,3,4,5,5,6,7,7,7}   #结果{2, 3, 4, 5, 6, 7} 表明集合不允许重复
print(s)
'''使用内置函数set()'''
s1=set(range(6))     #内置函数与随机函数进行使用
print(s1)
print(set([3,4,53,56]))  #内置函数与列表一起使用
print(set((3,4,43,435))) #内置函数与元组一起使用
print(set('Python'))     #内置函数和字符串一起使用
print(set({124,3,4,4,5}))
'''空集合'''
s7=set()
print(s7)

#集合元素的判断操作
'''in 或 not in'''
s={10,20,30,405,60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

#集合元素的新增操作
'''调用add()方法，一次添加一个元素'''
s.add(80)
print(s)
'''调用update（）方法，一次至少添加一个元素'''
s.update({200,400,300,100})
print(s)

#集合元素的删除操作
'''调用remove（）方法，一次删除一个指定元素，指定元素不存在抛出keyerror'''
s.remove(100)
print(s)
'''调用discard()方法，一次删除一个指定元素，如果指定元素不存在不抛异常'''
s.discard(100)
print(s)
'''调用pop()方法，一次只删除一个任意元素'''
s.pop()
print(s)
s.pop()
print(s)
'''调用clear（）方法，清空集合'''
s.clear()
print(s)