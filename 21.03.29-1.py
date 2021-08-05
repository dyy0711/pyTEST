#集合之间的关系
'''两个集合是否相等（元素相同，就相等）'''
s={10,20,30,40}
s1={30,40,20,10}
print(s==s1)
print(s!=s1)
'''一个集合是否是另一个集合的子集'''
print('一个集合是否是另一个集合的子集')
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))
print(s3.issubset(s1))
'''一个集合是否是另一个集合的超集'''
print('一个集合是否是另一个集合的超集')
print(s1.issuperset(s2))
print(s1.issuperset(s3))
'''两个集合是否患有交集'''
print('两个集合是否有交集')
print(s2.isdisjoint(s3))      #有交集结果为False
s4={100,200,300}
print(s2.isdisjoint(s4))      #没有交际结果为True

#集合的数学操作
'''交集操作'''
s1={10,20,30,40}
s2={20,30,40,50,60}
print('交集操作')
print(s1.intersection(s2))
print(s1 & s2)        #intersection()与&等价，交集操作
'''并集操作'''
print('''并集操作''')
print(s1.union(s2))
print(s1 | s2)        #union()与|等价，交集操作
'''差集操作'''
print('差集操作')
print(s1.difference(s2))
print(s1-s2)          #difference()与-等价，差集操作
'''对称差集'''
print('对称差集')
print(s1.symmetric_difference(s2))
print(s1^s2)           #symmetric_difference与^等价，对称差集操作

#集合生成式
'''列表生成式'''
lst=[i*i for i in range(6)]
print(lst)
'''集合生成式'''
s={i*i for i in range(6)}
print(s)