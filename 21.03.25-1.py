#流程控制语句break---用于结束循环结构，通常与分支结构if一起使用
'''从键盘录入密码，最多录入三次，如果正确就结束循环'''
for item in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
print('while实现')
i=0
while(i<3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        a=0
        break
    else:
        print('密码错误')
        i+=1