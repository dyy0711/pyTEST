import random
from random import randint
while True:
    guess=random.randint(1,100)
    count=0
    num=int(input('在1到100内猜一个数'))
    a=0
    b=100
    while True:
        if count==10:
            print('小垃圾~~都这么多次还没猜对')
        if num==guess:
            print('你猜对啦！')
            break
        elif num>guess:
            print('大傻瓜！你猜大啦~')
            b=num
            count+=1
        elif num<guess:
            print('小傻瓜！你猜小啦~')
            a=num
            count+=1
        else:
            pass
        print('在',a,'到',b,'之间')
        num=int(input('猜一个数：'))
    bool=input('小笨蛋，还想再玩一局吗？y/n\n')
    if bool=='y':
        pass
    elif bool=='n':
        break
    else:
        print('傻子！输错啦~不和你玩啦！byebye~')
        break