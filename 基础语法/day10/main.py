# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#print(__name__)
#变量名的查找规则（顺序）
    # 1.查找本地变量
    # 2.查找包含此函数的外部嵌套函数内部的变量
    # 3.全局变量
    # 4.内置变量
# a = 1
# b = 2
# def fx(b,c):
#     print(a,b,c)
#     print("全局变量字典：",globals())
#     print("局部变量字典：",locals())
#fx(3,4)
# 练习1：p1到p2（包含p2）中b个步长的所有值求和
#方法一：参数长度未知，用元组来传参
'''
def test1(*args):
    value = 0
    varb = None
    if len(args) == 1:
        varb = range(args[0])
    elif len(args) == 2:
        varb = range(args[0],args[1])
    elif len(args) == 3:
        varb = range(args[0],args[1],args[2])
    else:
        return None
    for index in varb:
        value += index
    return  value
'''
#方法一升级（参数直接代入）
# def test1(*args):
#     return sum(range(*args))
#方法二：参数长度有范围，可以用缺省参数定义形参
'''
def test1(start,stop=None,step=1):
    value = 0
    if stop == None:
        stop = start
        start = 0
    return sum(range(start,stop,step))
'''
#print(test1(5)) # 一个参数 从0到5，步长1
#print(test1(4,6)) # 两个参数 从4到6，步长1
#print(test1(5,10,2)) # 三个参数 从5到10，步长2
#print(test1(1,2,3,4,5)) # 五个参数 报错

# 2.语句学习
    # 2.1 global # 声明变量为全局变量
    # 2.2 nonlocal # 声明变量为外部嵌套函数的变量
# v = 100
# def outter():
#     v = 200
#     print("outter里的v =",v)
#     def inner():
#         #global v # 声明该作用域内的v为全局的v
#         nonlocal v # 声明该作用域内的v为外部嵌套函数作用域的v，如有2层以上嵌套，则定义为最近一层嵌套
#         v += 1
#         print("inne里的v =",v)
#     inner()
#     print("调用inner后，outter里的v =",v)
#outter()
#print("全局里的v =",v)


# 练习2：自己写一个max函数
    # 方法一
'''
def myMax(a,*args):
    if len(args) == 0:
        m = a[0]
        for i in range(1,len(a)):
            if m < a[i]:
                m = a[i]
        return m
    else:
        m = a
        for va in args:
            if m < va:
                m = va
        return m
'''
    # 方法二
# def myMax(a,*args):
#     def _myMax(*args):
#         #print("args len =",len(args))
#         m = args[0]
#         for va in args:
#             if m < va:
#                 m = va
#         return m
#     if len(args) == 0:
#         return _myMax(*a) # a 是 [6, 8, 3, 5] _myMax中的len(args) = 1 ; 前面加*后就是拆解成 6, 8, 3, 5 _myMax中的len(args) = 4
#     else:
#         return _myMax(a,*args)
# print(myMax([6,8,3,5]))
# print(myMax(1,2))
# print(myMax(1,8,3,1,9))


# 课后练习：
# 1.创建一个列表L = []
# 写一个函数input_number读取数据放入列表L中
    # 方法一
# L = []
# def input_number():
#     while True:
#         i = int(input("请输入数字（-1结束）："))
#         if i == -1:
#             break
#         L.append(i) # 此时我并没有改变L的绑定关系，所以没操作变量，不需要声明全局变量
# input_number()
# print("刚才输入的所有数字：",L)
    # 方法二
L = []
def input_number():
    lst = []
    while True:
        i = int(input("请输入数字（-1结束）："))
        if i == -1:
            break
        lst.append(i)
    global L # 该情况改变了变量，所以要声明全局变量L，不然会创建L为局部变量
    L = lst # 改变变量
input_number()
print("刚才输入的所有数字：",L)