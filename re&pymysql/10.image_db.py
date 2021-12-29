"""
二进制文件存储
"""

import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='grade', charset='utf8')
cur = db.cursor()

# 存储图片
# with open('image.jpg', 'rb') as f:
#     data = f.read()
# try:
#     sql = "update stu set image = %s where name = 'Jame';"
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取存储的图片
sql = "select image from stu where name = 'Jame';"
cur.execute(sql)
data = cur.fetchone()
with open('hello.jpg', 'wb') as f:
    f.write(data[0])

# 关闭游标及数据库
cur.close()
db.close()
