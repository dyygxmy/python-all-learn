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
gen = (x**2 for x in range(1,5))
print(gen) # <generator object <genexpr> at 0x0000018692674EB0>
it = iter(gen)
print(next(it)) # 1
print(next(it)) # 4
print(next(it)) # 9
print(next(it)) # 16
print(next(it)) # StopIteration



