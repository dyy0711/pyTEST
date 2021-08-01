#字典中元素的获取
'''第一种方式，使用[]'''
scores={'张三':100,'李四':98,'王五':45}
print(scores['张三'])
#print(scores['陈六'])  该种方法查找的键值不存在的时候会报错。
'''第二种方式，使用get()方法'''
print(scores.get('张三'))
print(scores.get('陈六'))  #执行结果为None,不报错
print(scores.get('麻七',99))  #99是在查找‘麻七’所对的value不存在时，提供一个默认值。 

#key 的判断
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

#字典的删除
del scores['张三']  #删除指定的键值对
print(scores)
scores.clear()
print(scores)      #清空字典中的元素

#字典元素的新增
scores={'张三':100,'李四':98,'王五':45}
scores['陈六']=98    #新增元素
print(scores)
scores['陈六']=100   #元素的修改
print(scores)

#获取字典视图的三个方法
'''获取所有的key'''
scores={'张三':100,'李四':98,'王五':45}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))    #将所有的key组成的视图转成列表
'''获取所有的value'''
values=scores.values()
print(values)
print(type(values))
print(list(values))
'''获取所有的key-value对'''
items=scores.items()
print(items)
print(type(items))
print(list(items))   #转换之后的列表元素是由元组组成的

#字典的遍历
scores={'张三':100,'李四':98,'王五':45}
for item in scores:
    print(item,scores[item],scores.get(item))

#字典的特点
'''key不允许重复，value是可以重复的'''
d={'name':'张三','name':'王五'}    #key值不允许重复，张三被覆盖
print(d)
d={'name':'张三','nickname':'王五'}    #value是可以重复的
print(d) 
'''字典中的元素是无序的'''
'''字典中的key必须是不可变对象'''
'''字典也可以根据需要动态地伸缩'''
'''字典会浪费较大的内存，是一种使用空间换时间的数据结构'''

#字典生成式
'''内置函数zip()'''
items=['Fruits','Books','Others']
prices=[96,78,85,100,120]
d={item:price for item ,price in zip(items,prices)}
print(d)
