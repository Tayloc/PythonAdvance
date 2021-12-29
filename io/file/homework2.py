"""
编写一个程序，向一个文件中写入如下内容：
1. 2019-1-1 18:18:18
2. 2019-1-1 18:18:19
ctrl-c  过5秒
3. 2019-1-1 18:18:24
循环每隔一秒写入一次，序号从1排列
ctrl-c结束程序，下次启动程序，序号要与之前的衔接
"""

import time

f = open('log.txt', 'a+')

f.seek(0, 0)

n = 0
for line in f:
    n += 1

while True:
    try:
        n += 1
        time.sleep(1)
        data = "%d.%s" % (n, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write((data + '\n'))
        f.flush()  # 随时查看
    except KeyboardInterrupt:
        break
