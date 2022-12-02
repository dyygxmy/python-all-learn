# *-encoding:utf8-*
# 创建二级子进程处理僵尸

import os

# 创建一级子进程

pid1 = os.fork()

if pid1 < 0:
    print("创建一级子进程失败")
elif pid1 == 0:
    pid2 = os.fork()
    if pid2 < 0:
        print("创建二级子进程失败")
    elif pid2 == 0:
        print("做另一件任务")
    else:
        # 一级子进程退出，使二级子进程成为孤儿
        os._exit(0)
else:
    os.wait() # 等待一级子进程退出 不用担心阻塞，一级子进程创建二级子进程后马上退出
    print("父进程在做的事")