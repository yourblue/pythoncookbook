"""
将字符串转化成日期
"""
import datetime as dt

x = '2017-12-21'
# 字符串转化成时间,性能很差，涉及大量时间字符串处理的时候，建议自行实现转化的方法
y = dt.datetime.strptime(x, '%Y-%m-%d')
print(y)
# 时间转化成字符串
d = dt.datetime.today()
nice_d = dt.datetime.strftime(d, '%A %B %d,%Y')
print(nice_d)


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return dt.datetime(int(year_s), int(mon_s), int(day_s))
