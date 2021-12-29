"""
僵尸进程：子进程先于父进程退出，父进程又没有处理子进程的退出状态，此时子进程就会成为僵尸进程
特点：僵尸进程虽然结束，但是会存留部分PCB在内存中，大量的僵尸进程会浪费系统的内存资源

如何避免僵尸进程产生
    使用wait函数处理子进程退出
        pid, status = os.wait()
            功能：在父进程中阻塞等待子进程退出
            返回值：pid 退出的子进程的PID  status 子进程退出状态
    创建二级子进程处理僵尸
        父进程创建子进程，等待回收子进程
        子进程创建二级子进程然后退出
        二级子进程称为孤儿，和原来父进程一同执行事件
    通过信号处理子进程退出
        原理：子进程退出时会发送信号给父进程，如果父进程忽略子进程信号，
        则系统就会自动处理子进程退出
        方法：使用signal模块在父进程创建子进程前写如下语句：
            import signal
            signal.signal(signal.SIGCHID, signal.SIG_IGN)
        特点：非阻塞，不会影响父进程运行。可以处理所有子进程退出
"""

# import os, sys
#
# # 使用wait函数处理子进程退出
# pid = os.fork()
# if pid < 0:
#     print("Error")
# elif pid == 0:
#     print("Child PID:", os.getpid())
#     sys.exit("子进程退出")
# else:
#     """
#     os.wait() 处理僵尸进程
#     """
#     pid, status = os.wait()
#     print("pid:", pid)
#     print("status:", status)  # 子进程退出状态 * 256
#
#     while True:  # 父进程不退出
#         pass


# 创建二级子进程处理僵尸
# import sys
# from time import sleep
# import os
#
#
# def f1():
#     for i in range(3):
#         sleep(2)
#         print("写代码")
#
#
# def f2():
#     for i in range(2):
#         sleep(4)
#         print("测代码")
#
#
# pid = os.fork()
#
# if pid < 0:
#     print("error")
# elif pid == 0:
#     child_pid = os.fork()
#     if child_pid < 0:
#         print("error")
#     elif child_pid == 0:
#         f1()
#     else:
#         sys.exit("一级子进程退出")
# else:
#     os.wait()  # 等一级子进程退出
#     f2()


# 信号处理僵尸
import os, sys
import signal

# 子进程退出时父进程忽略退出行为，子进程由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    print("Child PID:", os.getpid())
    sys.exit()
else:
    while True:
        pass
