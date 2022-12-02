# 包中的__init__.py文件

# 示例
# import mypack # mypack包被加载! 120
# help(mypack)
# Help on package mypack:
#
# NAME
#     mypack - 这是一个用来测试用的包，此处是标题
#
# DESCRIPTION
#     此包内有两个函数:
#     以下略...
#
# PACKAGE CONTENTS
#     games (package)
#     menu
#     office (package)
#
# FUNCTIONS
#     fx()
#
# DATA
#     name1 = '我是mypack内的name1变量'
#
# FILE
#     e:\users\administrator\pycharmprojects\python全套学习\day14\mypack\__init__.py


# print(dir(mypack)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
                    # '__name__', '__package__', '__path__', '__spec__', 'fx', 'name1']
# mypack.fx()

# 如下会将mypack/__init__.py内__all__列表一同导入
# from mypack import *    # mypack包被加载! 120
                        # mypack/games/__init__.py被导入
                        # mypack/menu被导入

# 如下会先导入mypack，再导入games，再导入contra/tanks
# import mypack.games.contra  # mypack包被加载! 120
                            # mypack/games/__init__.py被导入
                            # 魂斗罗模块被加载!
# from mypack.games import tanks  # mypack包被加载! 120
                                # mypack/games/__init__.py被导入
                                # 坦克大战模块被加载!

# 示例包的相对导入
# import mypack.games.contra as C
# C.gameover()




# try-except语句
# def get_score():
#     try:
#         score = int(input("请输入学生的成绩 :"))
#     except:
#         print("输入错误")
#         return 0
#     if 0<=score<=100:
#         print("输入正确")
#         return score
#     return 0
# score = get_score()
# print("学生的成绩是 :",score)


# 在程序调用层数较深时，向主调函数传递错误信息需要层层的return返回比较麻烦，所以用异常处理机制
# def f1():
#     print("开始房子打地基...")
#     raise ValueError("挖出文物")
#     print("地基完工")
# def f2():
#     print("开始盖房子地面以上部分")
#     raise ZeroDivisionError("要建高压线")
#     print("房子完工")
# def f3():
#     """第二承包商找人干活"""
#     f1()
#     f2()
# def build_house():
#     """第一承包商再承包出去"""
#     f3()
# try:
#     build_house()
# except ValueError as err:
#     print("房子没盖成，因为",err)
# except ZeroDivisionError as err:
#     print("房子没盖成，因为",err)
# else:
#     print("房子盖好了")


# 课后练习:
#     1.一个球从100米高度落下，每次落地后反弹高度为原高度的一半，再落下
#         1) 写程序算出皮球从第10次落地后反弹高度是多少
#         2) 球共经过多少米路程
# import time as T
# import sys
# sys.setrecursionlimit(999999999)
# s = 0.0
# def cur_bouncesHigh(h,count):
#     global s
#     h = h/2
#     s += h
#     print("第%d次弹起的高度为 : %.50f" %(count,h))
#     # T.sleep(1)
#     if round(h,50) == 0:
#         return
#     else:
#         cur_bouncesHigh(h,count+1)
# cur_bouncesHigh(100,1)
# print("总路程 :%f"%(s*2+100))
#     2.打印九九乘法表:
#         1*1=1
#         1*2=2 2*2=4
#         1*3=3 2*3=6 3*3=9
#         ....
#         1*9=9 2*9=18 ................... 9*9=81
# line 一行
# column 一列
# for li in range(1,10):
#     for co in range(1,li+1):
#         pro = co*li
#         interval = "  "
#         if pro < 10:
#             interval = "   "
#         msg = "%d * %d = %d%s"%(co,li,pro,interval)
#         if co == li:
#             print(msg)
#         else:
#             print(msg,end="")
#     3.分解质因数:
#         输入一个正整数，分解质因数
#         如:
#             输入90则打印:
#                 90 = 2*3*3*5
#         (质因数是指最小能被原数整除的素数(不包含1))
# value = int(input("请输入一个正整数 :"))
# list_coft = []
# def get_coefficient(n):
#     coes = False
#     for x in range(2,n):
#         if n%x == 0:
#             coes = True
#             print(n,x)
#             n = int(n/x)
#             list_coft.append(x)
#             get_coefficient(n)
#             break
#         if not coes and x == n-1: # 前面遇到有因数就break了，能到这里就是最后没有因数了，记录下最后这个数
#             print(n)
#             list_coft.append(n)
# get_coefficient(value)
# print(list_coft)