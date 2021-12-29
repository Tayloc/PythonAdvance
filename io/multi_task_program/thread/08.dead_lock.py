"""
死锁发生的必要条件
    互斥条件：指线程对所分配到的资源进行排他性使用，即在一段时间内某资源只由一个进程占用
            如果此时还有其他进程请求资源，则请求者只能等待，直至占有资源的进程用毕释放
    请求和保持条件：指线程已经保持至少一个资源，但又提出了新的资源请求，而该资源已被其他
            进程占有，此时请求线程阻塞，但又对自己已获得的其他资源保持不放
    不剥夺条件：指线程已获得的资源，在未使用完之前，不能被剥夺，只能在使用完时由自己释放
            通常CPU内存资源是可以被系统强行调配剥夺的
"""

from time import sleep
from threading import Thread, Lock


# 交易类
class Account:
    def __init__(self, name, balance, lock):
        self.name = name  # 表示用户
        self.balance = balance  # 表示用户存款
        self.lock = lock  # 用户自己的锁

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance


#   产生两个账户
Tom = Account('Tom', 5000, Lock())
Alex = Account('Alex', 8000, Lock())


# 转账过程
def transfer(from_, to, amount):
    if from_.lock.acquire():  # 锁住自己账户
        from_.withdraw(amount)  # from_账户减少
        sleep(0.5)
        if to.lock.acquire():  # 锁住对方账户
            to.deposit(amount)  # to账户加钱
            to.lock.release()  # to账户解锁
        from_.lock.release()  # from_账户解锁
    print("%s给%s转账%d" % (from_.name, to.name, amount))


# transfer(Tom, Alex, 4000)

t1 = Thread(target=transfer, args=(Tom, Alex, 2000))
t2 = Thread(target=transfer, args=(Alex, Tom, 3500))
t1.start()
t2.start()
t1.join()
t2.join()
