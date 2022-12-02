def myyield():
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成器函数调用结束") # 调用函数时不会打印这句
gen = myyield()

# print(gen) # <generator object myyield at 0x000001892F024EB0>

# for x in myyield():
#     print(x) # 2
                # 3
                # 5
                # 7
                # 生成器函数调用结束

it = iter(gen)
x = next(it)
print(x) # 2