"""
去除序列中出现的重复元素，但仍保持剩下的元素顺序不变
通常情况下，队列表的去重，需要构建一个集合，但是这样得到的结果会被打乱。
"""


def dedupe(items, key=None):
    """
    Data Dedupe(重复资料删除)
    去除重复项
    :param items: 要去除重复项的序列
    :param key: 没有参数key的时候，是只有当序列中的元素可哈希的时候才能这么做。
    :return: 没有重复项的序列
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1, 3, 2, 5, 1, 9, 1, 5]
print(list(dedupe(a)))
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
