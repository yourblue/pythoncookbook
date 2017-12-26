import itertools

"""
普通的切片操作无法对迭代器进行操作，因为不知道长度是多少，所以只能使用itertools。但是itertools会消耗迭代器，无法恢复
"""


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# c[10:20]

for x in itertools.islice(c, 10, 20):
    print(x)
