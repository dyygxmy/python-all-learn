# 迭代器示例
# L = [2,3,5,7]
# it = iter(L) # 用iter返回一个迭代器用it绑定
# print(it) # <list_iterator object at 0x0000020AE49C68B0>
# print(next(it)) # 2 用next来获取L中的元素
# print(next(it)) # 3
# print(next(it)) # 5
# print(next(it)) # 7
# print(next(it)) # StopIteration 通知next调用者，已无数据

# 迭代器示例 2
# it = iter(range(1,20,3))
# print(next(it)) # 1
# print(next(it)) # 4
# print(next(it)) # 7
# print(next(it)) # 10
# print(next(it)) # 13
# print(next(it)) # 16
# print(next(it)) # 19
# print(next(it)) # StopIteration

# 用for循环来访问可迭代对象中的数据
# for x in L:
#     print(x)

# 用while循环与for循环一样能访问可迭代对象中的数据
# it = iter(L)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break


# 生成器练习:
# 1.写一个生成器函数my_integer(n)生成1到n的整数
# 注: my_integer函数里面的while循环与外面的for循环并非嵌套关系，
    # 类似于下棋一样，一人一步来，for循环循环到一个x，
    # 然后x到my_integer函数中去循环生成一个数出来，for下次循环也一样
# def my_integer(n):
#     i = 1
#     while i < n:
#         yield i
#         i += 1
# for x in my_integer(1000000):
#     print(x)
# 2.写一个生成器函数myodd(start,stop)用于生成start到stop结束的所有奇数
# def myodd(start,stop):
#     for x in range(start,stop):
#         if x % 2:
#             yield x
# L = [x for x in myodd(1,10)]
# print(L) # [1,3,5,7,9]
# for x in myodd(10,20):
#     print(x,end=" ") # 11 13 15 17 19


# 生成表达式示例
# gen = (x**2 for x in range(1,5))
# print(gen) # <generator object <genexpr> at 0x0000018692674EB0>
# it = iter(gen)
# print(next(it)) # 1
# print(next(it)) # 4
# print(next(it)) # 9
# print(next(it)) # 16
# print(next(it)) # StopIteration


# 练习:
#     写一个程序，读入任意行的文字数据，当输入窄时结束输入
#     打印带行号的输入结果:
#     如:
#         请输入: hello<回车>
#         请输入: tarena<回车>
#         请输入: bye<回车>
#         请输入:  <回车 >
#         输出结果:
#             第1行 : hello
#             第2行 : tarena
#             第3行 : bye
# def input_text():
#     msg = []
#     while True:
#         put = input("请输入 :")
#         if len(put) == 0:
#             return msg
#         else:
#             msg.append(put)
# def main():
#     for t in enumerate(input_text(),1):
#         print("第%d行 : %s"%t)
# main()


# u = '\u2310'
# print(type(u),u)

# msg2 = "\u20b0\u20b1\u20b2\u20b3"
# print(msg2)

# B = b'\x41'
# print(len(B),B)

# B = bytes([0x41,0x42,0x43])
# print(B) # b'ABC'

# B = bytes(range(0x41,0x61))
# print(B) # b'ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`'

# B = bytes(5)
# print(B) # b'\x00\x00\x00\x00\x00'

# B = bytes("hello","utf8")
# print(B) # b'hello'
# B_zh = bytes("你好","utf8")
# print(B_zh) # b'\xe4\xbd\xa0\xe5\xa5\xbd'


# bytes 的运算示例
# a = bytes('1234',"utf8")
# b = bytes('7890',"utf8")
# print(a+b) # b'12347890'
# B = b'ABCDE'
# print(0x41 in B) # True
# print(B[3]) # 68
# print(B[3:]) # b'DE'
# print(B[::3]) # b'AD'
# print(B[:1:3]) # b'A'


# 序列的方法示例
# help(bytes)
# B = b'ABCDEFGH'
# print(B.center(20)) # b'      ABCDEFGH      '


# bytes 与 str 转换示例
# b = "你好".encode("utf8")
# print(b) # b'\xe4\xbd\xa0\xe5\xa5\xbd'
# s = b.decode('utf8')
# print(s) # 你好

# print("\u328b") # ㊋
# print("\u328b\u328c\u328d\u328e\u328f") # ㊋㊌㊍㊎㊏
#
# def set_str_len(init,le):
#     init = init[2:] # 去掉前面的0x
#     # print(type(init),len(init),init)
#     if len(init) < le:
#         for x in range(le-len(init)):
#             init = "0" + init
#     return init
# msg = ""
# for x in range(0xd800): # 到0xd800就超出了
#     msg = "\\u"+set_str_len(hex(x),4)
#     # print(type(msg),msg) # <class 'str'> \u9998
#     # print(x,msg.encode().decode("utf8")) # 9998 \u9998
#     print(x,hex(x),msg,msg.encode().decode("unicode-escape")) # 55291 0xd7fb ퟻ

# msg = "\\u20b0\\u20b1\\u20b2\\u20b3"
# print(msg.encode().decode("unicode-escape")) # ₰₱₲₳


# print(bytearray()) # bytearray(b'')
# print(bytearray(3)) # bytearray(b'\x00\x00\x00')
# print(bytearray([65,66,67])) # bytearray(b'ABC')
# print(bytearray("ABC是大写的abc","utf8")) # bytearray(b'ABC\xe6\x98\xaf\xe5\xa4\xa7\xe5\x86\x99\xe7\x9a\x84abc')


# ba = bytearray(b'abcdefg')
# print(ba[0]) # 97
# print(ba[1::2]) # bytearray(b'bdf')
# ba[1::2] = bytearray(b'XXX')
# print(ba) # bytearray(b'aXcXeXg')

# 课后练习:
# 1.用生成器函数生成斐波那契数列的前n个数:
#   1 1 2 3 5 8 13 ....
#   1) 输出前20个数
#   2) 求前30个数的和
# def fibonacci(n):
#     la = 1
#     s = 1
#     for x in range(n):
#         if x > 1:
#             s += la # 新值等于前两个值之和 s = s(5) + la(3)
#             la = s - la # 计算出新值生成后前一个的值，用于下个循环 la = s(8) - la(3)
#         yield s
# def print_fibo(n):
#     yie = fibonacci(20)
#     for _ in range(n):
#         print(next(yie),end=" ")
#     print()
# def sum_fibo(n):
#     yie = fibonacci(n)
#     s = 0
#     for _ in range(n):
#         s += next(yie)
#     return s
# print_fibo(20)
# print(sum_fibo(30))
# 2.写程序打印杨辉三角(只打6层)
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1
def oneline(x,n,l):
    s = []
    for _ in range(n-1-x):
        s.append(" ")
    # print(x)
    if x:
        for index in range(n-x-1,n-x+2*x,2): # 值后接一个空格，所以下标的步长为2
            # print(x,index)
            if index > 0:
                up_l = l[index-1]
            else:
                up_l = " "
            try:
                up_r = l[index+1]
            except IndexError:
                up_r = " "
            # print("up_l:%s up_r:%s"%(up_l,up_r))
            if up_l != " ":
                if up_r != " ":
                    s.append(str(int(up_l)+int(up_r)))
                    s.append(" ")
                else:
                    s.append(up_l)
            else:
                if up_r != " ":
                    s.append(up_r)
                    s.append(" ")
    else:
        s.append("1")
    for _ in range(n-1-x):
        s.append(" ")
    return s

def yanghui(n):
    l = []
    for x in range(n):
        l = oneline(x,n,l)
        for va in l:
            print(va,end="")
        print()
yanghui(6)




# print("----------")
# lt = [1,2,3]
# print(lt[-2])