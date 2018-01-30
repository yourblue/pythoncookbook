"""
需要读写以gzip或bz2格式压缩过的文件中的数据
"""
import gzip
import bz2

with gzip.open('something.gz', 'rt') as f:
    text = f.read()
#     写入数据
    f.write(text)
# rt换成wt
with bz2.open('something.bz2', 'rt') as f:
    text = f.read()
    f.write(text)
