#流程控制语句continue（用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用）
'''输出1-50之间的所有5的倍数'''
for i in range (1,51):
    if (i%5!=0):
        continue
    print(i)
#else语句
for item in range(3):
    pwd=input('请输入密码')
    if(pwd=='8888'):
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，三次密码均错误')

print('while-else')
a=0
while(a<3):
    pwd=input('请输入密码')
    if(pwd=='8888'):
        print('密码正确')
        break
    else:
        print('密码错误')
        a+=1
else:
    print('对不起，三次密码均错误')