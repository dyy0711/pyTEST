'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以贵大为4种：
--Tag
--NavigableString
--BeautifulSoup
--Comment
'''

from bs4 import BeautifulSoup
file=open('bd3.html','rb') 
html=file.read()
file.close()
print(html)
bs=BeautifulSoup(html,'html.parser')
print(bs)
print(bs.title)