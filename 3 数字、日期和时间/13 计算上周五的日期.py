"""
一周中上一次出现某天时的日期
"""
import datetime as dt
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_by_day(day_name, start_date=None):
    if start_date is None:
        start_date = dt.datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(day_name)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - dt.timedelta(days=days_ago)
    return target_date


now = dt.datetime.now()
print(now)
print(now + relativedelta(weekday=MO))
print(now + relativedelta(weekday=MO(-1)))
