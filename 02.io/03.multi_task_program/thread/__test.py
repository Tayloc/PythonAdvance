"""
测试单进程(single_process.py)，多进程(multi_process.py)，多线程(multi_thread.py)效率
"""


# CPU密集型程序
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


# IO密集型程序
def io():
    write()
    read()


def write():
    f = open('test', 'w')
    for i in range(1800000):
        f.write("Hello World\n")
    f.close()


def read():
    f = open('test')
    lines = f.readlines()
    f.close()
