"""
将名称映射到序列中，通过名称来访问元素
命名元组：比字典的内存开销小，不可变的，支持普通元组所支持的操作
"""
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['name', 'shares', 'prices'])
sub = Subscriber('qiuhy@qq.com', 2019, 111)
print(sub)
print(sub.name)
print(len(sub))
print(sub[1])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Subscriber(*rec)
        total += s.shares + s.prices
    return total


s = Subscriber('ACME', 100, 13)
print(s)
s=s._replace(shares=10)
print(s)

