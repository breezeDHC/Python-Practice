#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
from datetime import datetime,timezone,timedelta
import re
def to_timestamp(dt_str,tz_str):
    dt_now = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    li = re.split(':',tz_str)
    if tz_str[3] == '+':
        tzone = int(li[0][-1])
    else:
        tzone = -int(li[0][-1])
   #利用match求时区信息
   # g = re.match(r'^UTC(\+|\-\d{1,2})\:00$',tz_str)
   # now = dt_now.replace(tzinfo = timezone(timedelta(hours = int(g(1)))))
    now = dt_now.replace(tzinfo = timezone(timedelta(hours = tzone)))
    return now.timestamp()
a = to_timestamp('2015-6-1 08:10:30','UTC+7:00')
b = to_timestamp('2015-5-31 16:10:30','UTC-09:00')
print(a)
print(b)
