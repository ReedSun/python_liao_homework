#写一个能处理去掉=的base64解码函数

# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):

    return base64.b64decode(s+b"="*(4-len(s)%4))
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')