import os
import sys
from time import sleep
pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print("子进程:",os.getpid())
    sleep(2)
    sys.exit(5)
else:
    p,status = os.wait()
    print(p,status)
    print(os.WEXITSTATUS(status))
    while True:
        pass