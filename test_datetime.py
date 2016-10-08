# -*- coding:utf-8 -*-

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):

    sun_datatime = datetime.strptime(dt_str,"%Y-%m-%d %H:%M:%S")  #把str格式的时间转化为datetime格式的时间
    re_sun = re.compile(r"(UTC)(.*)(:00)")   #建立提取时区的正则表达式
    sun_timezone = int(re_sun.match(tz_str).group(2))  #提取时区
    sun_timezone = timezone(timedelta(hours=sun_timezone))  #创建时区
    sun_datatime_timezone = sun_datatime.replace(tzinfo=sun_timezone)  #强制设置timezone
    print(sun_datatime_timezone.timestamp())   #把datetime转化为timestamp
    return(sun_datatime_timezone.timestamp())

# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
