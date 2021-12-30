"""
python线程GIL(全局解释器锁)问题
    由于python解释器设计中加入了解释器锁，导致python解释器同一时刻只能解释执行一个线程，大大降低了线程的执行效率
    因为遇到阻塞时线程会主动让出解释器，去解释其他线程。所以python多线程在执行多阻塞高延迟IO时可以提升效率，其他情况并不能对效率有所提升
GIL问题建议
    尽量使用进程完成无阻塞的并发行为
    不使用c作为解释器
"""
from __test import *
from threading import Thread
from time import time

jobs = []

tm = time()

# for i in range(10):
#     t = Thread(target=count, args=(1, 1))
#     jobs.append(t)
#     t.start()
#
# for i in jobs:
#     i.join()
#
# print("Thread CPU:", time() - tm)  # Thread CPU: 6.533556222915649

for i in range(10):
    t = Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

print("Thread IO:", time() - tm)  # Thread IO: 9.993696928024292
