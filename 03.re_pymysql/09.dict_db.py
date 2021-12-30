"""
将单词本存入数据库

1.创建数据库dict（utf8）
    CREATE DATABASE dict CHARSET=utf8;
2.创建数据表words,将单词和单词解释分别存入不同的字段
    create table words (id int PRIMARY KEY auto_increment,word char(32),mean text);
3.将单词存入words单词表
"""
import re
import pymysql

f = open('dict.txt')  # 打开文件

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='dict', charset='utf8')

# 创建游标对象
cur = db.cursor()

# data = f.readline()
# temp = data.split(' ')
# word = temp[0]  # 获取单词
# mean = ' '.join(temp[1:]).strip()  # 获取单词的解释

sql = "insert into words (word,mean) values (%s,%s)"

for line in f:
    # 列表中只有一项，取列表第一项
    tup = re.findall(r"(\S+)\s+(.*)", line)[
        0]  # (\S+)匹配单词;\s+匹配单词和解释之间的空格;(.*):匹配0个或多个任意字符，用括号括起来：匹配当中但凡有子组的话findall匹配只显示子组对应部分
    try:
        cur.execute(sql, tup)  # 元组的第一项和第二项分别传给word和mean
        db.commit()
    except:
        db.rollback()

f.close()

# 关闭数据库
cur.close()
db.close()
