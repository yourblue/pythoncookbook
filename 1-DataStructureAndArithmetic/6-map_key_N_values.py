"""
将键映射到多个值的字典
collections.defaultdict
"""
from collections import defaultdict

# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# l = [x for x in range(1, 5)]
# print(l)
if __name__ == "__main__":
    d = defaultdict(list)
    pairs = {'a': ['1', '4', '6'], 'b': '2', 'c': '3'}
    for key, value in pairs.items():
        d[key].append(value)
    print(d)
