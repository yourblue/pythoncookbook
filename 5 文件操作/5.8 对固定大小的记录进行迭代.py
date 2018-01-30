"""
想对一系列固定大小的记录或数据块进行迭代
主要是针对二进制模式的可以使用这个，对于文本模式的直接按行读取更靠谱一点
"""
from functools import partial

RECORD_SIZE = 32

with open('something.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        pass
