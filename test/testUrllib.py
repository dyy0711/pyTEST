import urllib.request
# response=urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

url='https://www.douban.com'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
