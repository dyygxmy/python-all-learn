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
#     # print(mk)
#     struct_time = t.localtime(mk)
#     # print(struct_time)
#     print("出生那天星期 :",struct_time.tm_wday+1)
#     print("你已经出生天数 :",int((t.mktime(t.localtime())-mk)/(24*60*60)))
# yuB()