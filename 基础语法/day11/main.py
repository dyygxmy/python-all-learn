# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# def func1():
#     def func2():
#         print("this is",func1,func2)
#         return 0
#     return func2
#print(func1()())
#print(func1()())
# 两次调用的fuc1是一样的，因为只创建了一次，两个的func2不一样，因为创建了两次
# this is <function func1 at 0x000001D7B71DC790> <function func1.<locals>.func2 at 0x000001D7B71DADC0>
# 0
# this is <function func1 at 0x000001D7B71DC790> <function func1.<locals>.func2 at 0x000001D7B71DAEE0>
# 0


# myadd = lambda x,y:x+y
# print(myadd(2,5))
# print(myadd("abc","def"))


# 练习：
# 1.写一个lambda表达式，判断这个数的2次方+1能否被5整除，如果整除返回True，否则返回False
# fx = lambda n:(n*n+1)%5==0
# print(fx(4))
# print(fx(3))
# 2.写一个lambda表达式，求两个变量的最大值
# # mymax = lambda x,y:max(x,y)
# mymax = lambda x,y:x if x>y else y #if表达式
# print(mymax(55,63))

# def fx(f,x,y):
#     r = f(x,y)
#     print(r)
# fx((lambda a,b:a+b),100,200)
# fx((lambda x,y:x**y),3,4)

# x=100
# y=200
# s="x+y"
# v = eval(s)
# print(s,"=",v) #x+y = 300

# s="list(range(10))"
# t=eval(s)
# print(s,t) #list(range(10)) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(eval("x+y",{'x':10,'y':20})) #30
# print(eval("x+y",{'x':10,'y':20},{'x':1,'y':2})) #3
# print(eval("x+y",{'x':10,'y':20},{'x':1})) # 21
# s="[x**2 for x in range(10) if x%3==0]"
# print(eval(s)) #[0, 9, 36, 81]

# s="""
# x=100
# print("hello")
# x+=1
# print(x)
# """
# print(s)
# exec(s)

# g = {}
# l = {}
# while True:
#     s = input("请输入语句: ~# ")
#     if s == "exit":
#         break
#     exec(s,g,l)
# print(g)
# print(l)

# n = 10
# print(sum(range(n+1)))

# 练习：
#     求： 1+1/2+1/4+1/8 + ... 1/2**n
# n=100
# print(sum([1/2**x for x in range(n+1)])) #使用列表推导式


# def power2(x):
#     return x**2
# for x in map(power2,range(1,10)):
#     print(x) #1 4 9 16 25 36 49 64 81
# print(sum(map(power2,range(1,10))))
# for x in map(pow,range(1,11),range(10,0,-1)):
#     print(x)

# for a in range(10,0,-1):
#     print(a)

# 练习：
# 1.求 1**2 + 2**2 + 3**2 + ... 9**2的和
# 2.求 1**3 + 2**3 + 3**3 + ... 9**3的和
# 3.求 1**9 + 2**8 + 3**7 + ... 9**1的和
# print(sum(map(pow,range(1,10),[2]*9))) #285
# print(sum(map(pow,range(1,10),[3]*9))) #2025
# print(sum(map(pow,range(1,10),range(9,0,-1)))) #11377

# def isodd(x):
#     return x%2 == 1
# for x in filter(isodd,range(10)):
#     print(x)

# l = [x for x in filter(lambda x:x%2==0,range(10))]
# print(l)

# L = [5,-2,-4,0,3,1]
# L2 = sorted(L)
# print(L2) # [-4,-2,0,1,3,5]
# L3 = sorted(L,reverse=True)
# print(L3)
# L4 = sorted(L,key=abs)
# print(L4) #[0, 1, -2, 3, -4, 5]

names = ['Tom','Jerry','Spike','Tyke']
# 能否根据名字长度进行排序
# L = sorted(names,key=len)
# print(L) # ['Tom', 'Tyke', 'Jerry', 'Spike']
# 反转排序
# def fr(s):
#     return s[::-1]
# # L = [x for x in map(fr,names)]
# # print(L) # ['moT', 'yrreJ', 'ekipS', 'ekyT'] 依据该字符串对names进行排序
# L5=sorted(names,key=fr)
# print(L5) # ['Spike', 'Tyke', 'Tom', 'Jerry']


# 用递归函数输出1~10的整数
# def fx(n):
#     print(n)
#     if n >= 10:
#         return
#     n+=1
#     fx(n)
# fx(1)

# 求100+99+98+....+1
# def mySum(n):
#     if n == 1:
#         return 1
#     return n + mySum(n-1)
# print(mySum(100)) # 5050


# 课后练习：
# 1.编写函数myfac(x)计算x的阶乘x!
    # 5! = 5*4*3*2*1
    # print(myfac(5)) # 120
# def myfac(x):
#     if x == 1:
#         return x
#     return x*myfac(x-1)
# print(myfac(5))
# 2.写程序算出1~20的阶乘的和
    # 1!+2!+....+20!
# print(sum(map(myfac,range(1,21))))
# 3.已知有列表：
    # L = [[3,5,8],10,[[13,14],15],18]
    # 1) 写一个函数print_list(list)打印出列表中所有数字
    # print_list(L)
# L = [[3,5,8],10,[[13,14],15],18]
# def getList(L2,myList):
#     if type(myList) is list:
#         for x in myList:
#             getList(L2,x)
#     elif type(myList) is int:
#         L2.append(myList)
# def print_list(myList):
#     L2 = []
#     getList(L2,myList)
#     return L2
# print(print_list(L))
    # 2) 写一个函数sum_list(list)返回列表中所有数字的和
    # print(sum_list(L)) # 86
# def sum_list(myList):
#     return sum(print_list(myList))
# print(sum_list(L))
    # 注：
    # type(x) 可以返回一个变量的类型
    # type(20) is int # True
    # type([1,2,3]) is list # True
    # print(isinstance(2,(int,list))) # True
    # print(isinstance([1,2,3],(int,list))) # True
    # print(isinstance(2,int)) # True
    # print(isinstance([1,2,3],list)) # True

# 4.开始学生信息管理项目
# 需要两个函数：
# input_student()返回学生信息的字典的列表
# 调用时等待用户输入，输入姓名为空时结束
# output_student(lst) 以表格方式打印学生信息
# 学生信息：
# 姓名(name) str
# 年龄(age) int
# 成绩(score) int
title_list = ['name','age','score']
head = "+----------+----------+----------+"
# body = "|----------|----------|----------|"
def input_student():
    L = []
    while True:
        name = input("请输入学生姓名 : ")
        if len(name) == 0:
            return L
        age = input("请输入学生年龄 : ")
        score = input("请输入学生成绩 : ")
        L.append({title_list[0]:name,title_list[1]:age,title_list[2]:score})
# print(input_student())
def output_student(lst):
    print(head)
    print(getBodyStr(title_list))
    print(head)
    for x in lst:
        print(getBodyStr([x[title_list[0]],x[title_list[1]],x[title_list[2]]]))
    print(head)
def getBodyStr(lst):
    str1 = ""
    ini = "|          "
    len_ini = len(ini)
    for x in lst:
        len_x = len(x)
        index = (int)((len_ini-1)/2)-(int)((len_x-1)/2)
        str1 = str1 + ini[:index] + x + ini[index+len(x):]
    str1 += "|"
    return str1
# L = ["safs","jkdsabj","dsauiiisa"]
# print(getBodyStr(L))
L2 =input_student()
print(L2)
output_student(L2)
