"""
进程对象属性
"""

from multiprocessing import Process
import time


def tm():
    for i in range(3):
        time.sleep(2)
        print(time.ctime())


# p = Process(target=tm)
# print("Name:", p.name)  # 打印进程默认名称

p = Process(target=tm, name='Dec')

# daemon设置父子进程的退出关系:如果设置为True则子进程会随父进程的退出而结束
# 要求必须在start()前设置
# 如果daemon设置成True通常就不会使用join()
p.daemon = True

p.start()

# 打印子进程name
print("Name:", p.name)  # Name:Dec

# 打印子进程pid
print("PID:", p.pid)  # 对应子进程PID

# 查看p对应的进程是否在生命周期(活着)
print("is alive:", p.is_alive())  # 返回bool值


