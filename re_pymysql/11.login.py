"""
编写一个程序模拟注册和登录的过程

创建一个user表 包含 用户名和密码字段
    CREATE TABLE user (id int PRIMARY KEY auto_increment,name VARCHAR(32) NOT NULL,passwd VARCHAR(32) NOT NULL);
应用程序中模拟注册和登录功能
注册则输入用户名密码将用户名密码存入数据库(用户名不能重复)
登录则进行数据库比对，如果有该用户则打印登录成功否则让重新输入
"""

import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='grade', charset='utf8')
cur = db.cursor()


# 注册
def register():
    name = input("用户名：")
    passwd = input("密码：")
    # 判断用户名是否重复
    sql = "select * from user where name = '%s'" % name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql = "insert into user (name,passwd) values (%s,%s)"
        cur.execute(sql, [name, passwd])
        db.commit()
        return True
    except:
        db.rollback()
        return False


def login():
    name = input("用户名：")
    passwd = input("密码：")
    sql = "select * from user where name='%s' and passwd = '%s'" % (name, passwd)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True


while True:
    print("""
            ===============
            1.注册    2.登录
            ===============
    """)
    cmd = input("输入命令：")
    if cmd == '1':
        # 执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == '2':
        # 执行登录
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("功能尚未实现")
# 关闭数据库
cur.close()
db.close()
