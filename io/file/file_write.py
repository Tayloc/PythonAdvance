"""
写入文件

write(string)
功能：把文本数据或二进制数据块的字符串写入到文件中去
参数：要写入的内容
    如果需要换行要自己在写入内容中添加\n

writelines(str_list)
功能：接收一个字符串列表作为参数，将它们写入文件
参数：要写入的内容列表
"""

# 打开文件
# f = open('test', 'w')
# f = open('img.jpg', 'wb')
f = open('test', 'a')  # 追加

# 写操作
# f.write("hello Tom\n".encode())
# f.write("emm，what?".encode())

# 将列表写入 人为添加换行
list_ = ['hello world\n', 'hello python']
f.writelines(list_)

f.close()
