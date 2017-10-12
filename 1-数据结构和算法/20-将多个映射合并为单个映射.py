"""
多个映射合并成单个映射

"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])  # 如果有重复的，会采用第一个里面的值
