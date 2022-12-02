# 此程序示意sys.stdin的用法

import sys

s = sys.stdin.read(10) # 默认从键盘获取数据
print(s)
s2 = sys.stdin.read(10)
print(s2)

s3 = sys.stdin.read() # 如果未指定长度，会一直读下去，输入多少内容都不会结束 (Crtl + D 结束输入)
print(s3)