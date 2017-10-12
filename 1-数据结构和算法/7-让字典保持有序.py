"""
创建一个字典，当对其进行迭代或者序列化的时候，能够控制其中元素的顺序
OrderedDict是普通字典的两倍大小，因此使用的时候，如果数据量特别大，应该仔细考虑下
"""
from collections import OrderedDict
import json

if __name__ == "__main__":

    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['span'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    print(json.dumps(d))
