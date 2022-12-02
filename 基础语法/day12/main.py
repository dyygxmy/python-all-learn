# 闭包示例
# def make_power(y):
#     def fn(x):
#         return x**y
#     return fn
# pow2 = make_power(2)
# pow3 = make_power(3)
# print("5的平方是 :",pow2(5)) # 5的平方是 : 25
# print("2的3次方是 :",pow3(2)) # 2的3次方是 : 8

# 装饰器示例
# def mydeco(fn): # 装饰器函数
#     fn()
#     def fx():
#         print("hello world!")
#     return fx
# @mydeco # 下面函数带入mydeco被fn绑定，然后函数绑定mydeco的返回值
# def hello(): # 被装饰函数
#     print("hello tarena!")
# # hello = mydeco(hello) # 此时将hello绑定在了mydeco返回的函数上
#                         # 此种做法可以用装饰器@语法解决
# hello() # 调用者

# 存取钱小程序
# def msg_send(fn):
#     def fy(name,x):
#         fn(name,x)
#         print("短信 :",name,"发生了",x,"元的操作，余额是XXX") # 余额提醒放在取款之后
#     return fy
# def priv_check(fn): # 装饰器函数，在fn调用之前加一个权限验证功能，不变动原函数及调用过程
#     def fx(name,x):
#         print("正在权限验证...") # 权限验证放在存/取钱之前
#         fn (name,x)
#     return fx
# @priv_check
# def save_money(name,x): # 存钱
#     print(name,"存钱",x,"元")
# @msg_send
# @priv_check
# def withdraw(name,x): # 取钱
#     print(name,"正在办理取钱",x,"元的业务")
# save_money("小张",200)
# save_money("小赵",500)
# withdraw("小李",300)

# 函数的文档字符串示例
# def myFun(a,b):
#     """
#     这就是文档字符串
#     三引号里面文档字符串还可以换行
#     这是最后一行
#     """
#     print("test")
# help(myFun)

# 函数的__doc__属性示例
# def cba():
#     "这是一个文档字符串123" # 只有第一个引号内的文档内容是文档字符串
#     "这已不是一个文档字符串456"
# print(cba.__doc__) # 这是一个文档字符串123

# import math # 导入数学计算模块
# print(math) # <module 'math' (built-in)>
# help(math) # 查看模块内的变量、函数、类等

# 1.输入一个圆的半径，打印出这个圆的面积
# def myS(r):
#     return math.pi*math.pow(r,2)
# print("面积是 :",myS(float(input("请输入半径 :"))))
# 2.输入一个圆的面积，打印出这个圆的半径
# def my_r(S):
#     return math.sqrt(S/math.pi)
# print("半径是 :",my_r(float(input("请输入面积 :"))))

# import os
# print(dir(os))
# print(dir())

# 练习:
# 1.请编写函数fun(n)，其功能是计算并输出下列多项式的和
# Sn = 1/1! + 1/2! + ... + 1/n!
# import math
# # 方法一:
# def fun(n):
#     l = []
#     for x in range(n+1):
#         l.append(1/math.factorial(x))
#     return sum(l)
# # 方法二:
# def fun2(n):
#     return sum(map(lambda x : 1/math.factorial(x),range(n+1)))
# print(fun(20))
# print(fun2(20))
# 2.请编写函数fun(n)，其功能是计算下列多项和并返回
# S = x + x**2/2! + x**3/3! +...+x**n/n!
# import math
# # 方法一:
# def fun(x,n):
#     l = []
#     for i in range(n+1):
#         l.append(math.pow(x,i)/math.factorial(i))
#     return sum(l)
# # 方法二:
# def fun2(x,n):
#     return sum(map(lambda i : math.pow(x,i)/math.factorial(i),range(n+1))) # 使用了一个闭包 调用了外面的x
# print(fun(3.1,10))
# print(fun2(3.1,10))


# 课后练习:
# 1.已知有5位朋友在一起
# 第五位朋友比第四个大2岁
# 第四位朋友比第三个大2岁
# 第三位朋友比第二个大2岁
# 第二位朋友比第一个大2岁
# 第一个说他今年10岁
# 编写程序算出第5人几岁
# 2.改写之前的学生信息管理项目源码，要求带有操作界面：
# +------------------------------------+
# | 1) 添加学生信息              |
# | 2) 显示所有学生的信息     |
# | 3) 删除学生信息              |
# | 4) 修改学生成绩              |
# | 5) 按学生成绩高低来显示  |
# | 6) 按学生成绩低高来显示  |
# | 7) 按学生年龄高低显示     |
# | 8) 按学生年龄低高显示     |
# | q) 退出                          |
# +------------------------------------+
# 请选择 :
# 要求每个功能至少写一个函数与之相对应

def show_menu():
    print("+------------------------------------+")
    print("| 1) 添加学生信息                    |")
    print("| 2) 显示所有学生的信息              |")
    print("| 3) 删除学生信息                    |")
    print("| 4) 修改学生成绩                    |")
    print("| 5) 按学生成绩高低来显示            |")
    print("| 6) 按学生成绩低高来显示            |")
    print("| 7) 按学生年龄高低显示              |")
    print("| 8) 按学生年龄低高显示              |")
    print("| q) 退出                            |")
    print("+------------------------------------+")

title_list = ['name', 'age', 'score']
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
        L.append({title_list[0]: name, title_list[1]: age, title_list[2]: score})

def output_student(lst):
    print(head)
    print(getBodyStr(title_list))
    print(head)
    for x in lst:
        print(getBodyStr([x[title_list[0]], x[title_list[1]], x[title_list[2]]]))
    print(head)

def getBodyStr(lst):
    str1 = ""
    ini = "|          "
    len_ini = len(ini)
    for x in lst:
        len_x = len(x)
        index = (int)((len_ini - 1) / 2) - (int)((len_x - 1) / 2)
        str1 = str1 + ini[:index] + x + ini[index + len(x):]
    str1 += "|"
    return str1

def delete_student(lst=[]):
    name = input("请输入需要删除的学生姓名 :")
    for i in lst:
        if i["name"] == name:
            lst.remove(i)
            return lst

def mySort(lst,key,rev):
    def myKey(lst):
        return lst[key]
    return sorted(lst,key=myKey,reverse=rev)

def main():
    docs = []
    while True:
        # 显示菜单
        show_menu()
        # 让用户做出选择
        s = input("请选择 :")
        # 根据用户做出选择处理相应的事情
        if s == 'q':
            return
        elif s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':
            docs = delete_student(docs)
        elif s == '4':
            pass
        elif s == '5':
            docs = mySort(docs,"score",True)
        elif s == '6':
            docs = mySort(docs,"score",False)
        elif s == '7':
            docs = mySort(docs,"age",True)
        elif s == '8':
            docs = mySort(docs,"age",False)
main()