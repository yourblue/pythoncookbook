"""
找出当月的日期范围
"""
import datetime as dt
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = dt.datetime.today().replace(day=1)
    # monthrange(year,month)返回的日历从头开始不是本月的空白部分，和当月的天数
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + dt.timedelta(days=days_in_month)
    return start_date, end_date


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step
