"""
pymysql读操作示例
"""

import pymysql

# 连接数据库，生成数据库对象
db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='grade', charset='utf8')

# 创建游标对象
cur = db.cursor()

# sql语句
sql = "select * from stu where gender='m';"

# 执行sql语句
cur.execute(sql)

# 执行正确后cur调用函数获取结果

# one_row = cur.fetchone()  # 获取一个查询结果
# print(one_row)  # 元组
#
# many_row = cur.fetchmany(2)  # 获取多个查询结果
# print(many_row)

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)

# 关闭游标
cur.close()

# 关闭数据库对象
db.close()
