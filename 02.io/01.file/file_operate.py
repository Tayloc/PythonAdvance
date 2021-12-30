"""
获取文件描述符
01.file.fileno()
    通过IO对象获取对应的文件描述符

文件管理函数
    1.获取文件大小
        os.path.getsize(01.file)
    2.查看文件列表
        os.listdir(dir)
    3.查看文件是否存在
        os.path.exists(01.file)
    4.判断文件类型
        os.path.isfile(01.file)
    5.删除文件
        os.remove(01.file)
"""

import os

print(os.path.getsize('file_operate.py'))

print(os.listdir('../day02'))

print(os.path.exists('test'))

print(os.path.isfile('test'))

os.remove('test')
