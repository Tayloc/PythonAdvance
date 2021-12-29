"""
flags参数扩展
    使用函数：re模块调用的匹配函数。如：re_pymysql.compile,re_pymysql.findall,re_pymysql.search...
    作用：扩展丰富正则表达式的匹配功能
    常用flag
        A == ASCII  元字符只能匹配ascii码
        I == IGNORECASE 匹配忽略字母大小写
        S == DOTALL 使.可以匹配换行
        M == MULTILINE  使^$可以匹配每一行的开头结尾位置
        X == VERBOSE    为正则添加注释
"""
import re

s = """Hello 
北京
"""

# 只能匹配ASCII编码
# regex = re_pymysql.compile(r'\w+', flags=re_pymysql.A)

# 不区分大小写
# regex = re_pymysql.compile(r'[a-z]+', flags=re_pymysql.I)

# 使.可以匹配换行
# regex = re_pymysql.compile(r'.+', flags=re_pymysql.S)

# ^,$匹配每一行开头结尾位置
# regex = re_pymysql.compile(r'^北京', flags=re_pymysql.M)
# regex = re_pymysql.compile(r'Hello $', flags=re_pymysql.M)

# 给正则分行注释
pattern = r"""\w+ # hello
\s+ # 匹配换行
\w+ # 北京
"""

regex = re.compile(pattern, flags=re.X | re.I)  # 既想给正则表达式加注释又想忽略大小写

l = regex.findall(s)
print(l)
