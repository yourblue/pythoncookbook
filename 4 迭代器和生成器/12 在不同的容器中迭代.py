from itertools import chain

"""
chain()最常见的用途是想一次性对所有的数据进行操作，但是这些数据在不同的集合中
不要求集合类型必须一致
比将各个序列加在一起然后再迭代要更加高效
"""
active_items = set()
inactive_items = set()
for item in chain(active_items, inactive_items):
    pass
