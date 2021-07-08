'''爬取豆瓣电影Top250的基本信息，包括电影的名称、豆瓣评分、评价数、电影概况、电影链接等'''
#-*-codeing=utf-8 -*-
from bs4 import BeautifulSoup     #网页解析，获取数据
import re      #正则表达式，进行文字匹配
import urllib.request,urllib.error    #制定URL，获取网页数据
import xlwt    #进行excel操作的
import sqlite3   #进行SQLite数据库操作

def main():
    baseurl='https://movie.douban.com/top250?start='
    #1.爬取网页
    datalist=getData(baseurl)
    #2.逐一解析数据
    #3.保存数据
    savepath='.\\豆瓣电影Top250.xls'
    saveDate(savepath)
    askURL(baseurl)

#爬取网页   
def getData(baseurl):
    datalist=[]
    for i in range(0，10):    #调用获取页面信息的函数10次（range函数左闭右开）
        url=baseurl+str(25*i)
        html=askURL(url)     #保存获取到的网页源码 
        #2.逐一解析数据

    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    #模拟浏览器头部信息，向豆瓣服务器发送消息
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    request=urllib.request.Request(url,headers=head)
    html=''
    try:
        response=urllib.request.Request(request)
        html=response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    #return


#保存数据
def saveDate(savepath):
    pass


if __name__=='__main__':
    main()