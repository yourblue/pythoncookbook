"""
根据一个或多个字典中的值来对列表进行排序
"""
from operator import itemgetter
"""
也会选择使用lambda表达式替代itemgetter，但是itemgetter运行速度更快。他也同样适应min()和max()这样的函数
"""
rows = [{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, ]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)
