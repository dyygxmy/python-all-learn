# 练习:
#     已知有一个集合:
#     s = {"工商银行","建设银行","中国银行","农业银行"}
#     1.用for语句遍历集合中的元素并打印
#     2.将上面的for语句改写成while语句实现上面同样的功能
#         提示:用iter和next函数实现
s = {"工商银行","建设银行","中国银行","农业银行"}
for x in s:
    print(x)
print("--------------")
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        break