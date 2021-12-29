"""
re&pymysql 模块使用

regex = compile(pattern, flags=0)
    功能：生成正则表达式对象
    参数：
        pattern 正则表达式
        flags 功能标志位，扩展正则表达式的匹配；默认是0
    返回值：正则表达式对象

regex.findall(string,pos,endpos)
    功能：根据正则表达式匹配目标字符串内容
    参数
        string 目标字符串
        pos 截取目标字符串的开始匹配位置
        endpos 截取目标字符串的结束匹配位置
    返回值：匹配到的内容列表，如果正则表达式有子组则只能获取到子组对应的内容

re&pymysql.findall(pattern, string, flags=0)
    功能：根据正则表达式匹配目标字符串内容
    参数
        pattern 正则表达式
        string 目标字符串
        flags 功能标志位，扩展正则表达式的匹配
    返回值：匹配到的内容列表，如果正则表达式有子组则只能获取到子组对应的内容

re&pymysql.split(pattern, string, flags=0)
    功能：使用正则表达式匹配内容，切割目标字符串
    参数
        pattern 正则表达式
        string 目标字符串
        flags 功能标志位，扩展正则表达式的匹配
    返回值：切割后的内容列表

re&pymysql.sub(pattern, replace, string, max, flags=0)
    功能：使用一个字符串替换正则表达式匹配到的内容
    参数
        pattern 正则表达式
        replace 替换的字符串
        string 目标字符串
        max 最多替换几处，默认替换全部
        flags 功能标志位，扩展正则表达式的匹配
    返回值：替换后的字符串

re&pymysql.subn(pattern, replace, string, max, flags=0)
    功能：使用一个字符串替换正则表达式匹配到的内容
    参数
        pattern 正则表达式
        replace 替换的字符串
        string 目标字符串
        max 最多替换几处，默认替换全部
        flags 功能标志位，扩展正则表达式的匹配
    返回值：替换后的字符串和替换了几处
"""

import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+"  # 正则表达式

# re模块调用findall
l = re.findall(pattern, s)
print(l)

# compile 对象调用findall
regex = re.compile(pattern)
l = regex.findall(s, 0, 12)
print(l)

# 按照正则表达式匹配内容切割字符串
l = re.split(r'[:,]', s)
print(l)

# 替换目标字符串
s = re.sub(r':', '-', s, 1)
print(s)
