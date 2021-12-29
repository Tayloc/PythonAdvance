"""
pymysql操作数据库基本流程演示
"""

import pymysql

# 连接数据库，生成数据库对象
db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='grade', charset='utf8')

# 创建游标对象
cur = db.cursor()

sql = "insert into stu values (7,'Emma',17,'w',76.5,'2019-8-8')"

# 执行sql语句
cur.execute(sql)

# 提交写操作，多次写操作可一同提交
db.commit()

# 关闭游标
cur.close()

# 关闭数据库对象
db.close()
