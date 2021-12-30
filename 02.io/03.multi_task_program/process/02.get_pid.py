"""
os.getpid()
    功能：获取一个进程的PID值
    返回值：返回当前进程的PID
os.getppid()
    功能：获取父进程的PID号
    返回值：返回父进程的PID
os._exit(status)
    功能：结束一个进程
    参数：进程的终止条件
sys.exit([status])
    功能：退出进程
    参数：整数 表示退出状态；字符串 表示退出时打印内容
"""

import os, sys

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:", os.getpid())
    print("Get parent PID:", os.getppid())
else:
    print("Get child PID:", pid)
    print("Parent PID:", os.getpid())

os._exit(0)  # 退出进程
sys.exit("退出")  # 退出进程
# print("exit test")
