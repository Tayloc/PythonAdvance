"""
pymysql写操作示例（insert update delete）
"""

import pymysql

# 连接数据库，生成数据库对象
db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='grade', charset='utf8')

# 创建游标对象
cur = db.cursor()

# 写数据库
try:
    # 写sql语句执行
    # 插入操作

    # name = input('Name:')
    # age = int(input('Age:'))
    # score = float(input("Score:"))
    # sql = "insert into stu (name,age,score) values ('%s',%d,%f)" % (name, age, score)

    # name = input('Name:')
    # age = input('Age:')
    # score = input('Score:')
    # sql = "insert into stu (name,age,score) values (%s,%s,%s)"
    # cur.execute(sql, [name, age, score])  # 通过列表给sql语句传值会自动地符合sql语句的格式

    # 修改操作
    # sql = "update stu set score = 90 where name = 'Abby'"
    # cur.execute(sql)

    # 删除操作
    sql = "delete from stu where score < 80"
    cur.execute(sql)

    db.commit()  # 提交
except Exception as e:
    db.rollback()  # 写数据库发生异常退回到commit执行之前的数据库状态
    print(e)

# 关闭游标
cur.close()

# 关闭数据库对象
db.close()
