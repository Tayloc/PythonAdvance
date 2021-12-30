"""
http请求测试
"""

from socket import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)
c, addr = s.accept()

print("Connect from", addr)
data = c.recv(4096)
print(data.decode())  # 打印http请求

# 将数据组织为响应格式
response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello World</h1>
"""
c.send(response.encode())

c.close()
s.close()

