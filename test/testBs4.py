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
t_list=bs.find_all('a')
print(t_list)