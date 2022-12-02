
# 此示例示意raise语法的用法

def make_except(n):
    # 假设n必须是0~100之间的数
    print("开始处理!")
    if n > 100: # 传过来的参数无效，怎么告诉调用者呢？
        raise ValueError # 直接告诉错误类型
    if n < 0:
        raise ValueError("输入的参数%d发生小于0的错误"%n) # 对告诉的错误类型加内容
    print("处理结束!")

value = int(input("请输入一个0~100的整数 :"))
try:
    make_except(value)
except ValueError as err:
    print("make_except 抛出了错误，此异常状态已处理")
    print("发生错误，错误值是 :",err)

print("程序正常完成!")