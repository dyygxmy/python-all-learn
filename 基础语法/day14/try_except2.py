#此示例示意用try-except语句来捕获异常

def div_apple(n):
    """此示例用分苹果来示意捕获异常"""
    print("%d个苹果你想要分给几个人？"%n)
    s = input("请输入人数 :")
    cnt = int(s) # 此处可能会引起ValueError类型的错误
    result = n/cnt
    print("每个人分了",result,"个苹果")

try:
    div_apple(10)
except (ValueError,ZeroDivisionError):
    # 以上两种错误都会用相同的方法来处理
    print("发生了错误，苹果被收回")

print("程序正常退出")