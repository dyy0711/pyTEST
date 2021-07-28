#嵌套循环（循环结构中又嵌套了另外的完整的循环结构，其中内层循环味外层循环的循环体执行）
'''输出一个三行四列的矩形'''
for i in range(1,4):           #行表，一次是一行
    for j in range(1,5):
        print('*',end='\t')    #不换行输出,  end''表示关闭在输出中默认的自动换行的行为
    print()                    #打印
'''打印一个直角三角形'''
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='')
    print()
'''打印九九乘法表'''
for i in range(1,10):    #表示行
    for j in range(1,i+1):
        print(j,'*',i,'=',j*i,end='\t')    #九九乘法表是列乘以行
    print()
#二重循环中的break和continue使用
'''二重循环中的break和continue用于控制本层循环'''
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()