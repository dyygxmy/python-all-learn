# 回顾day12

# 闭包
# def fn(x):
#     def re():
#         return x+1
#     return re()
# print(fn(3))

# 装饰器（不带参数）
# def dec(fn):
#     fn()
#     def fx():
#         print("装饰后")
#     return fx
# @dec
# def fn():
#     print("装饰前")
# fn()

# 装饰器（带参数）
# def dec(fn):
#     def fx(x):
#         print("x1:",x)
#         x = fn(x)
#         print("x2:", x)
#         x+=10
#         return x
#     print("x3:")
#     return fx
# @dec
# def fn(x):
#     print("x0:", x)
#     x+=1
#     return x
# print(fn(1))
# 打印顺序如下
# x3:
# x1: 1
# x0: 1
# x2: 2
# 12

# 文档字符串
# def fn():
#     "这就是文档字符串"
# print(fn.__doc__)



# day13开始

# time() 返回从计算机元年至当前时间的秒数的浮点数（UTC时间为准）
# sleep(secs) 让程序按给定秒数的浮点数睡眠一段时间
# gmtime([secs]) 将给秒数转换为用UTC表达的时间元组
# asctime([tuple]) 将时间元组转换为日期时间字符串
# mktime(tuple) 将本地日期时间元组转换为新纪元秒数时间（UTC为准）
# localtime([secs]) 将UTC秒数时间转换为日期元组（以本地时间为准）

# import time
# print(time.time()) # 1626180488.0723252
# print(time.gmtime())
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=13, tm_hour=12,
# tm_min=1, tm_sec=53, tm_wday=1, tm_yday=194, tm_isdst=0)
# print(time.gmtime(1626177713))
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=13, tm_hour=12,
# tm_min=1, tm_sec=53, tm_wday=1, tm_yday=194, tm_isdst=0)
# print(time.asctime()) # Tue Jul 13 20:30:53 2021
# myAsc = (2021,7,14,13,8,16,0,0,0)
# print(time.asctime(myAsc)) # Mon Jul 13 13:08:16 2021
# print(time.mktime(myAsc)) # 1626239296.0
# print(time.localtime(1626239296))
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=14, tm_hour=13,
# tm_min=8, tm_sec=16, tm_wday=2, tm_yday=195, tm_isdst=0)
# print(time.localtime())
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=13, tm_hour=20,
# tm_min=48, tm_sec=8, tm_wday=1, tm_yday=194, tm_isdst=0)


# 练习:
# 1.写一个程序，以电子时钟的格式显示时间
# HH:MM:SS
# import time as t
# def show_time():
#     while True:
#         struct_time_local = t.localtime()
#         # 方法一:用字符串来提取
#         '''
#         hh = str(struct_time_local.tm_hour)
#         if len(hh) == 1:
#             hh = "0" + hh
#         mm = str(struct_time_local.tm_min)
#         if len(mm) == 1:
#             mm = "0" + mm
#         ss = str(struct_time_local.tm_sec)
#         if len(ss) == 1:
#             ss = "0" + ss
#         print(hh,":",mm,":",ss)
#         '''
#         #方法二:用整型+表达式提取 开头加 \r 后面加 end="" 可以实现不换行，并光标回到开头打印(覆盖打印)
#         print("\r%02d:%02d:%02d"%(struct_time_local.tm_hour,struct_time_local.tm_min,struct_time_local.tm_sec),end="")
#         t.sleep(1)
# show_time()
# 2.写一个程序，输入你的生日，
# 1) 计算出你出生那天是星期几
# 2) 计算出你已经出生了多少天
# import time as t
# def yuB():
#     yy = int(input("请输入出生年 :"))
#     mm = int(input("请输入出生月 :"))
#     dd = int(input("请输入出生日 :"))
#     bir = (yy,mm,dd,0,0,0,0,0,0)
#     mk = t.mktime(bir)
#     # print("UTC时间的秒数 :",mk)
#     struct_time = t.localtime(mk)
#     # print(struct_time)
#     L = ["星期一",
#          "星期二",
#          "星期三",
#          "星期四",
#          "星期五",
#          "星期六",
#          "星期日"]
#     print("出生那天星期 :",L[struct_time.tm_wday])
#     # print("你已经出生天数1 :",int((t.mktime(t.localtime())-mk)/(24*60*60)))
#     print("你已经出生天数2 :", int((t.time()-mk) / (24 * 60 * 60)))
# yuB()

# sys 模块
import sys
def pathList_print():
    l = sys.path
    i = 0
    for x in l:
        print(i,x)
        i+=1
# pathList_print()
# 0 E:\Users\Administrator\PycharmProjects\python全套学习
# 1 E:\Users\Administrator\PycharmProjects\python全套学习
# 2 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python38.zip
# 3 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\DLLs
# 4 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib
# 5 C:\Users\Administrator\AppData\Local\Programs\Python\Python38
# 6 E:\Users\Administrator\PycharmProjects\python全套学习\venv
# 7 E:\Users\Administrator\PycharmProjects\python全套学习\venv\lib\site-packages

# print(sys.argv[0]) # E:/Users/Administrator/PycharmProjects/python全套学习/main.py

# print(sys.getrecursionlimit()) # 1000
# print(sys.setrecursionlimit(20000000)) # None
# print(sys.getrecursionlimit()) # 20000000

# 添加自定义模块目录
# sys.path.append("E:\\")
# pathList_print()
# import mymod
# mymod.testPrint()
# 0 E:\Users\Administrator\PycharmProjects\python全套学习
# 1 E:\Users\Administrator\PycharmProjects\python全套学习
# 2 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python38.zip
# 3 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\DLLs
# 4 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib
# 5 C:\Users\Administrator\AppData\Local\Programs\Python\Python38
# 6 E:\Users\Administrator\PycharmProjects\python全套学习\venv
# 7 E:\Users\Administrator\PycharmProjects\python全套学习\venv\lib\site-packages
# 0 E:\Users\Administrator\PycharmProjects\python全套学习
# 1 E:\Users\Administrator\PycharmProjects\python全套学习
# 2 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python38.zip
# 3 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\DLLs
# 4 C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib
# 5 C:\Users\Administrator\AppData\Local\Programs\Python\Python38
# 6 E:\Users\Administrator\PycharmProjects\python全套学习\venv
# 7 E:\Users\Administrator\PycharmProjects\python全套学习\venv\lib\site-packages
# 8 E:\
# this is mymod


# 随机模块
import random as R
# print(R.random()) # 0.6018314486429436
# print(R.uniform(5,6)) # 5.36897126278399
# print(R.randrange(0,11,2)) # 10
# print(R.choice([1,7,3,6,0,2])) # 7
# L = list(range(5))
# print(L) # [0, 1, 2, 3, 4]
# R.shuffle(L)
# print(L) # [4, 1, 3, 2, 0]
# print(R.sample(L,3)) # [3, 0, 1]


# 练习:
# 1.假设可以作为密码的字符有:
# A~Z
# a~z
# 0~9
# 空格和下划线
# 写一个程序，随机生成六位密码
# l_un = [' ','_','!','@','#','$','%','^','&']
# l_09 = [chr(x) for x in  range(ord('0'),ord('9')+1)] # chr : ASCII转字符  ord : 字符转ASCII
# l_AZ = [chr(x) for x in  range(ord('A'),ord('Z')+1)]
# l_az = [chr(x) for x in  range(ord('a'),ord('z')+1)]
# print(l_09)
# print(l_AZ)
# print(l_az)
# l_all = l_un + l_09 + l_AZ + l_az
# print(l_all)
# data = ""
# for _ in range(6):
#     data += R.choice(l_all)
# mima = ''.join(data) # join 将列表转换为字符串，中间用''内的内容隔开
# print(mima)



# 模块包调用
# 示例
# import mypack.menu # 导入mypack包里的menu模块
# mypack.menu.show_menu() # 调用menu里的函数
# import mypack.games.contra # 导入子包games里的contra模块
# mypack.games.contra.play() # 调用contra里的函数


# 课后练习:
# 1.编写一个闹钟程序，启动时设置定时时间（小时和分钟）
# 到时间后打印"时间到。。。。"然后退出程序
# import time as T
# set_H = int(input("请设定小时值 :"))
# set_M = int(input("请设定分钟值 :"))
# while True:
#     t_tuple_now = T.localtime(T.time())
#     # print(t_tuple_now)
#     print("\r设置时间 :",set_H,":",set_M,"当前时间 :",t_tuple_now.tm_hour,":",t_tuple_now.tm_min,end="")
#     #if t_tuple_now.tm_hour == set_H and t_tuple_now.tm_min == set_M: # 判断方式一
#     if (set_H,set_M) == t_tuple_now[3:5]: # 判断方式二
#         break
#     T.sleep(1)
# print("\n时间到...")
# 2.模拟斗地主发牌，扑克牌54张
# 花色:
# 黑桃('\u2660'),梅花('\u2663'),方块('\u2665'),红桃('\u2666')
# 数值:
# A2-10JQK
# 大小王
# 三个人，每人发17张牌，底牌留三张:
# 输入回车，打印第1个人的17张牌
# 输入回车，打印第2个人的17张牌
# 输入回车，打印第3个人的17张牌
# 再输入回车，打印出三张底牌
cardes_King = ["MAX","MIN"]
cardes_str = ['A','J','Q','K']
cardes_int = [str(x) for x in range(2,11)] + cardes_str
kinds = ['\u2660','\u2663','\u2665','\u2666']
# 赋值花色 方法一
cardes_all = [n+i for n in kinds for i in cardes_int]
# 赋值花色 方法二
# for x in cardes_int:
#     cardes_all.append('\u2660' + x)
#     cardes_all.append('\u2663' + x)
#     cardes_all.append('\u2665' + x)
#     cardes_all.append('\u2666' + x)
cardes_all += cardes_King
print(len(cardes_all),cardes_all)
import random as rd
# 方法一 洗牌后按顺序发给3人
rd.shuffle(cardes_all)
card_1 = cardes_all[:17]
card_2 = cardes_all[17:17*2]
card_3 = cardes_all[17*2:17*3]
cardes_all3 = cardes_all[17*3:]
# 方法二 随机抽牌发给3人
# card_1 = rd.sample(cardes_all,17)
# cardes_all1 = [x for x in cardes_all if x not in card_1]
# print(len(cardes_all1),cardes_all1)
# card_2 = rd.sample(cardes_all1,17)
# cardes_all2 = [x for x in cardes_all1 if x not in card_2]
# print(len(cardes_all2),cardes_all2)
# card_3 = rd.sample(cardes_all2,17)
# cardes_all3 = [x for x in cardes_all2 if x not in card_3]
# print(len(cardes_all3),cardes_all3)
input("请输入回车 :")
print("第1个人的"+str(len(card_1))+"张牌",card_1)
input("请输入回车 :")
print("第2个人的"+str(len(card_2))+"张牌",card_2)
input("请输入回车 :")
print("第3个人的"+str(len(card_3))+"张牌",card_3)
input("请输入回车 :")
print("最后"+str(len(cardes_all3))+"张底牌",cardes_all3)
