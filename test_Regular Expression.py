import re
input = input("请输入邮箱")
re_email = re.compile(r"^(\w+)@(\w+).com$")
result = re.match(re_email,input)
if result:
    print("您输入的邮箱名合法")
else:
    print("您输入的邮箱名不合法")
print("您的名字是%s" % result.group(1))
print("您使用的邮箱是%s" % result.group(2))