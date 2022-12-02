# *-encoding:utf8-*

import os
import sys
from time import sleep
pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print("子进程")
    sleep(2)
    sys.exit(2)
else:
    # 设置为非阻塞状态，循环处理查看子进程状态
    while True:
        p,status = os.waitpid(-1,os.WNOHANG) # 任意进程 非阻塞
        sleep(0.5)
        print("父进程")
        print(p,status)
    while True:
        pass