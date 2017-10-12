"""
根据某个特定的字段来分组迭代数据
需要先排序才能进行分组，

"""
from operator import itemgetter
from itertools import groupby

rows = [{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, ]

rows.sort(key=itemgetter('uid'))
for uid, item in groupby(rows, key=itemgetter('lname')):
    print(uid)
    for i in item:
        print('', i)
