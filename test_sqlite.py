# -*- coding: utf-8 -*-

import os
import sqlite3

# 在当前工作目录创建 test.db数据库文件，如果已创建了，原文件将会被删除
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)


# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    """返回指定分数区间的名字，按分数从低到高排序"""
    try:
        conn2 = sqlite3.connect(db_file)
        cursor2 = conn2.cursor()
        cursor2.execute("select * from user where score between %s and %s" % (low, high))
        result = cursor2.fetchall()
        result.sort(key=lambda y: y[2])
        values = []
        for x in result:
            values.append(x[1])
    finally:
        return values
        cursor2.close()
        conn2.commit()
        comm2.close()


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
