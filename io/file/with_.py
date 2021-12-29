"""
with执行清理操作，释放被访问的资源，比如有文件读写后自动关闭、线程中锁的自动获取和释放等
with语法格式
    with 生成对象的语句 [as target(s)]:
        with-body
通过with方法可以不用close()，因为with生成的对象在语句块结束后会自动处理
所以也就不需要close了，但是这个对象只能在with语句块内使用
"""

with open('day02.txt') as f:  # 生成文件对象
    data = f.read()
    print(data)
