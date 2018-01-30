"""
将二进制数据读取到一个可变缓冲区内，中间不经过任何拷贝环节
readinto是为已经存在的缓冲区填充内容，而不是分配新的内存，因此可以避免额外的内存消耗
"""
import os


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


with open('../files/something.bin', 'wb') as f:
    f.write(b'Hello,World')
buf = read_into_buffer('../files/something.bin')
buf[0:5] = b'Hallo'
print(buf)
print(buf[0:5])

