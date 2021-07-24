#程序结构
#顺序结构
'''把大象装冰箱一共分几步'''
print('-------程序开始-------')
print('1.把冰箱门打开')
print('2把大象放冰箱里')
print('3把冰箱门关上')
print('-------程序结束-------')
#测试对象的布尔值--布尔值函数bool()
#以下对象布尔值均为False，其他均为True
print('以下对象布尔值均为False，其他均为True')
print('False', bool(False))   #False布尔值为False
print('数值0',bool(0))        #数值0布尔值为False
print('None',bool())          #None布尔值为False
print('空字符串',bool(''))     #空字符串布尔值为False
print('空列表',bool([]))      #空列表布尔值为False
print('空列表',bool(list()))  #空列表布尔值为False
print('空元组',bool(()))      #空元组布尔值为False
print('空元组',bool(tuple())) #空元组布尔值为False
print('空字典',bool({}))      #空字典布尔值为False
print('空字典',bool(dict()))  #空字典布尔值为False
print('空集合',bool(set()))   #空集合布尔值为False
#选择结构
#单分支结构
money=1000   #余额
s=int(input('请输入取款金额')) #取款金额
if(money>=s):   #判断余额是否充足
   money=money-s
   print('取款成功，余额为：',money)
#双分支结构：if.....else,二选一执行
'''从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数'''
s=int(input('输入一个整数'))
if(s%2==1):    #条件判断奇偶性
    print(s,'是奇数')
else:
    print(s,'是偶数')
#多分支结构---多选一执行
'''
从键盘录入一个整数成绩，判断成绩范围
90-100 A
80-89  B
70-79  C
60-69  D
0-59   E
小于0或大于100为非法数据（不是成绩的有限范围）
'''
g=int(input('输入成绩'))
if(90<=g<=100):
    print('成绩为A')
elif(80<=g<=89):
    print('成绩为B')
elif(70<=g<=79):
    print('成绩为C') 
elif(60<=g<=69):
    print('成绩为D')
elif(0<=g<=59):
    print('成绩为E')
else:
    print('非法数据')
#嵌套if
'''
会员 >=200 8折
     >=100 9折
     不打折
非会员 >=200 9.5折
       不打折
'''
money=float(input('请输入消费金额'))
a=input('是否为会员')
if (a=='Y'):
    if(money>=200):
        print('支付金额为：',money*0.8)
    elif(100<=money<200):
        print('支付金额为：',money*0.9)
    else:
        print('支付金额为：',money)
else:
    if(money>=200):
        print('支付金额为：',money*0.95)
    else:
        print('支付金额为：',money)
#条件表达式
'''从键盘录入两个整数，比较两个整数的大小'''
n1=int(input('输入一个整数n1：'))
n2=int(input('输入一个整数n2：'))
if(n1>n2):
    print(n1,'大于',n2)
elif(n1==n2):
        print(n1,'等于',n2)
else:
    print(n1,'小于',n2)
print('使用条件表达式进行输出')    #使用条件表达式输出
print(str(n1)+'大于等于n2'+str(n2)   if(n1>=n2)   else  str(n1)+'小于等于'+str(n2))  '''
if为条件判断 
判断结果为True则执行条件判断左侧的内容
判断结果为False则执行条件判断右侧的内容'''
#pass语句，什么都不做，只是一个占位符，用到需要写语句的地方