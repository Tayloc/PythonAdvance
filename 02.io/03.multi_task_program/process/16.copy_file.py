"""
创建两个进程，分别复制文件的上半部分和下半部分到两个新的文件中
"""
import os
from multiprocessing import Process

size = os.path.getsize('img.jpg')  # 获取img.jpg文件的大小


def top_half():
    fr = open('img.jpg', 'rb')
    fw = open('top.jpg', 'wb')
    fw.write(fr.read(size // 2))
    fw.close()
    fr.close()


def lower_half():
    fr = open('img.jpg', 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fw.close()
    fr.close()


p1 = Process(target=top_half)
p2 = Process(target=lower_half)
p1.start()
p2.start()
p1.join()
p2.join()

