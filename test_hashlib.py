# coding=utf-8

import hashlib


def calc_md5(username, password):
    passwd_md5 = hashlib.md5()
    passwd_md5.update(password.encode("utf-8"))
    passwd_md5.update("ReedSun".encode("utf-8"))
    passwd_md5.update(username.encode("utf-8"))
    return passwd_md5.hexdigest()


def login(username, password):
    if calc_md5(username, password) == db[username]:
        print("%s登陆成功" % username)
    else:
        print("%s登陆失败，密码错误" % username)


def register(username, password):
    db[username] = calc_md5(username, password)

db = {}  # 模拟密码的数据库

register("sun", "123456")
register("jiang", "102115")
register("Reed", "852456")
login("sun", "123456")
login("jiang", "123456")
login("Reed", "852456")
