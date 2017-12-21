"""
时间方面的转换使用datetime模块来处理
更多的时间方面的处理可以使用dateutil模块来处理
"""
import datetime as dt

# 表示一个时间间隔
a = dt.timedelta(days=2, hours=6)
b = dt.timedelta(hours=4.5)
c = a + b
print(c)
print(c.days)
print(c.seconds)
print(c.max)
# 表示一个特定的日期和时间
x = dt.datetime(2017, 12, 1)
print(x + dt.timedelta(days=20))
print(dt.datetime.today())
print(dt.datetime.now())
print(dt.date.today())
print(dt.time.hour)
