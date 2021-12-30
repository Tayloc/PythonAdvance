"""
使用udp完成：客户端不断录入学生信息，将其发送到服务端，
在服务端，将学生信息写入到一个文件中，每个学生信息占一行
信息格式：id  name  age  score
id(int)  name(str)  age(int)  score(float)
"""

from socket import *
import struct

# 和客户端一致
st = struct.Struct('i32sif')

# udp套接字
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('0.0.0.0', 8882))

# 打开文件
f = open('exercise.txt', 'a')

while True:
    data, addr = s.recvfrom(1024)
    data = st.unpack(data)
    # 写入文件
    info = "%d %-10s %d %.1f\n" % data
    f.write(info)
    f.flush()
