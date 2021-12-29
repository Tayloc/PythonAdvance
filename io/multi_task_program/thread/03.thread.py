"""
自定义线程类
    创建步骤
        继承Thread类
        重写__init__方法添加自己的属性，使用super加载父类属性
        重写run方法
    使用方法
        实例化对象
        调用start自动执行run方法
        调用join回收线程
"""

from threading import Thread


# 自定义线程类
class ThreadClass(Thread):
    # 重写父类init
    def __init__(self, *args, **kwargs):
        self.attr = args[0]
        super().__init__()  # 加载父类init

    # 假设需要很多步骤完成功能
    def f1(self):
        print("step 1")

    def f2(self):
        print("step 2")

    # 重写run方法，逻辑调用
    def run(self):
        self.f1()
        self.f2()


t = ThreadClass('abc')
t.start()  # 自动运行run方法
t.join()
