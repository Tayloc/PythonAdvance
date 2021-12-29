"""
空洞文件
"""

f = open('test', 'wb')

f.write(b'start')
f.seek(1024 * 1024, 2)  # 从结尾向后移动1k
f.write(b'end')
# 文件test的大小是1k

f.close()
