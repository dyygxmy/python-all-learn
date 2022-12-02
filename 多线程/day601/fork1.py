# *-encoding:utf8-*
import os
from time import sleep
pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print("子进程")
    print("getpid:",os.getpid()) # 子进程自己获取自己的PID
    print("getppid:",os.getppid()) # 子进程获取父进程PID
else:
    sleep(1)
    p,status = os.wait()
    print(p,status)
    print(os.WEXITSTATUS(status))
    while True:
        pass