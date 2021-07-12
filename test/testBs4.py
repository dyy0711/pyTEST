'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以贵大为4种：
--Tag
--NavigableString
--BeautifulSoup
--Comment
'''
#import os
# from sys import path
# from bs4 import BeautifulSoup
# if os.path.exists('bd3.html'):
#     with open ('bd3.html','rb') as file:
#         html=file.read()
# else:
#     print('111')
# # file=open(r'D:\Github\pyTEST\123/bd3.html','rb') 
# # html=file.read()
# # file.close()
# print(html)
# bs=BeautifulSoup(html,'html.parser')
# print(bs)
# print(bs.title)

from re import findall
from bs4 import BeautifulSoup
file=open('./baidu.html','rb')
html=file.read()
# print(html)
bs=BeautifulSoup(html,'html.parser')
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))
# #print(bs.button)
# #1.Tag 标签及其内容；拿到它所找到的第一个内容
# print(bs.title.string)
# print(type(bs.title.string))
#2.NavigableString 标签里的内容（字符串）
# print(type(bs))    
# #3.BeautifulSoup   表示整个文档
# print(bs.name)
# print(bs.a.string)
# print(type(bs.a.string))
#4.Comment  是一个特殊的Navigablestring,输出的内容不包含注释符号


#----------------------------------------

#文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])


#文档的搜索
#(1) find_all()
#字符串过滤;会查找与字符串完全匹配的内容
# t_list=bs.find_all('a')
# print(t_list)

#正则表达式搜索:使用search()方法来匹配内容
# import re
# t_list=bs.find_all(re.compile('a'))
# print(t_list)

#方法:传入一个函数,根据函数的要求来搜索(了解)
# def name_is_exists(tag):
#     return tag.has_attr('name')
# t_list=bs.find_all(name_is_exists)
# print(t_list)


#2.kwargs  参数
# t_list=bs.find_all(id='head')
# for item in t_list:
#     print(item)

# t_list=bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# t_list=bs.find_all(href='http://news.baidu.com')
# for item in t_list:
#     print(item)


#3.text参数
# t_list=bs.find_all(text='hao123')
# for item in t_list:
#     print(item)

# t_list=bs.find_all(text=['hao123','地图','贴吧'])
# for item in t_list:
#     print(item)

# import re
# t_list=bs.find_all(text=re.compile('\d'))    #应用正则表达式来查找包含特定文本的内容(标签里的字符串)
# for item in t_list:
#     print(item)


#4.limit参数
# t_list=bs.find_all('a',limit=3)
# for item in t_list:
#     print(item)




#css选择器
# t_list=bs.select('title')    #通过标签来查找
# for item in t_list:
#     print(item)

# t_list=bs.select('.mnav')    #通过类名来查找
# for item in t_list:
#     print(item)

# t_list=bs.select('#u1')    #通过id来查找
# for item in t_list:
#     print(item)

# t_list=bs.select('a[class="bri"]')     #通过属性来查找
# for item in t_list:
#     print(item)

# t_list=bs.select('head>title')      #通过子标签来查找
# for item in t_list:
#     print(item)

t_list=bs.select('.mnav~.bri')
print(t_list[0].get_text())