"""
进程间通信
    1.必要性：进程间空间独立，资源不共享，此时在需要进程间数据传输时就需要特定的手段进行数据通信
    2.常用进程间通信方法：管道 消息队列 共享内存 信号 信号量 套接字

管道通信
    通信原理
        在内存中开辟管道空间，生成管道操作对象，多个进程使用同一个管道对象进行读写即可实现通信
    实现方法
        from multiprocessing import Pipe
        fd1, fd2 = Pipe(duplex = True)
            功能：创建管道对象
            参数：默认表示双向管道；如果为False表示单向管道
            返回值
                表示管道两端的读写对象
                如果是双向管道均可读写
                如果是单向管道fd1只读 fd2只写
        fd.recv()
            功能：从管道获取内容
            返回值：获取到的数据
        fd.send()
            功能：向管道写入内容
            参数：要写入的数据
"""

# 管道通信：multiprocessing中管道通信只能用于有亲缘关系进程中
# 管道对象在父进程中创建，子进程通过父进程获取

from multiprocessing import Process, Pipe

# 创建管道
fd1, fd2 = Pipe()


def app1():
    print("启动app1,请登录")
    print("请求app2 授权")
    fd1.send("app1 请求登录")  # 写入管道
    data = fd1.recv()
    if data:
        print("登录成功", data)


def app2():
    data = fd2.recv()  # 阻塞等待读取管道内容
    print(data)
    fd2.send(('Dave', '123'))  # 可以发送任意Python类型数据


p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()
