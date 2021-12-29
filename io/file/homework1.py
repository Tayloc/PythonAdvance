"""
编写一个文件拷贝程序，从终端输入一个文件
将文件保存在当前目录下
文件类型不确定（可能是文本文件，可能是二进制文件）
"""

# file_input = input("请输入文件名>>")
#
# f1 = open(file_input, 'rb')
# f2 = open('new_file.py', 'wb')
#
# f2.write(f1.read())
#
# f1.close()
# f2.close()

# 输入文件名
file_name = input("File:")

try:
    fr = open(file_name, 'rb')
except FileNotFoundError as e:
    print(e)
else:
    fw = open('file.jpg', 'wb')
    # 循环读取文件知道最后
    while True:
        data = fr.read(1024)
        if not data:  # 文件结束
            break
        fw.write(data)

    fr.close()
    fw.close()

