"""
pid = os.fork()
    功能：创建新的进程
    返回值：整数，如果创建进程失败返回一个负数，如果成功则在原有进程中返回新进程的PID，在新进程中返回0
"""

import os
from time import sleep

# 创建子进程
pid = os.fork()  # 子进程从fork的下一句开始执行

if pid < 0:
    print("Create process failed")
# 子进程执行的部分
elif pid == 0:
    sleep(2)
    print("The new process")
# 父进程执行的部分
else:
    sleep(3)
    print("The old process")

# 父子进程都会执行的部分
print("Fork test over")
