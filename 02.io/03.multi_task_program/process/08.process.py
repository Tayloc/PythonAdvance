"""
Process 给进程函数传参
"""

from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working..")


# 用元组给进程函数传参
# p = Process(target=worker, args=(2, 'Baron'))

# 用字典给进程函数传参
# p = Process(target=worker, kwargs={'name': 'Baron', 'sec': 2})

# 同时用元组和字典给进程函数传参
p = Process(target=worker, args=(2,), kwargs={'name': 'Baron'})

p.start()
p.join()
