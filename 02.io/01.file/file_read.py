"""
read([size])
功能：用来直接读取文件中字符
参数：如果没有给定size参数(默认值为-1)或者size值为负，文件
将被读取直至末尾；给定size最多读取给定数目个字符(字节)。
返回值：返回读取到的内容
注意：文件过大时候不建议直接读取到文件结尾，
读取文件结尾会返回空字符串。

read([size])
功能：用来读取文件中的一行
参数：如果没有给定size参数(默认值为-1)或者size值为负，
表示读取一行，给定size表示最多读取指定的字符(字节)。
返回值：返回读取到的内容

readlines([sizeint])
功能：读取文件中的每一行作为列表中的一项
参数：如果没有给定size参数(默认值为-1)或者size值为负，
文件将被读取直至末尾，给定size表示读取到size字符所在行为止。
返回值：返回读取到内容列表

文件对象本身也是一个可迭代对象，在for循环中可以迭代文件中的每一行。
"""

# 打开文件
f = open('test', 'r')

# read循环读取
# while True:
#     data = f.read(100)  # 每次最多读100个字符
#     # 读到文件结尾返回空字符串
#     if not data:
#         break
#     print(data)

# 读取一行内容
# data = f.readline(10)  # 读取第一行前10个字符
# print("一行内容：", data)
# data = f.readline()  # 把第一行剩余内容读完
# print("一行内容：", data)

# 将内容读取为列表
# data = f.readlines()
# print(data)

# f为可迭代对象
for i in f:
    print(i)  # 每次迭代一行内容

# 关闭
f.close()
