import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# size = 10000
# with open('../files/data', 'wb') as f:
#     f.seek(size - 1)
#     f.write(b'\x00')

m = memory_map('../files/data')
print(len(m))
print(m[0:10])
print(m[0])
m[0:11] = b'Hello,World'
m.close()
with open('../files/data', 'rb') as f:
    print(f.read(12))

