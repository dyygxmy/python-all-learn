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
except ValueError as err:
    print("报错信息 :",err) # invalid literal for int() with base 10: 'd'
    print("发生了值错误，苹果被收回")
except:
    print("发生了除值错误以外的错误，在此处理")
else:
    # 此处语句只在没发生异常时才会执行
    print("没有发生错误，草果分完了")
finally:
    # 此处的语句无论是否发生异常都会执行
    print("管你有没有错误，此处是必经之路")

print("程序正常退出")