"""
file_open.py
"""

# 打开文件，获取文件对象
try:
    # fd = open('../01.data_structure/binary_search.py', 'r')  # 以只读打开
    # fd = open('../01.data_structure/binary_search.py', 'w')  # 以只写方式打开
    # fd = open('../01.data_structure/binary_search.py', 'a')  # 以追加方式打开
    """
    普通的文本文件 既可以使用文本方式打开也可以使用二进制方式打开
    二进制文件则必须以二进制方式打开
    """
    fd = open('../../01.data_structure/binary_search.py', 'rb')  # 二进制方式
    print(fd)
except Exception as e:
    print(e)

# 读写文件

# 关闭文件
else:
    fd.close()
