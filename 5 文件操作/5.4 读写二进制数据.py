"""
需要读写二进制文件，比如图像、声音文件等
rb:读二进制文件
wb:写二进制文件
在做索引和迭代操作时，字节串返回的时该字节的整数值而不是字符串
如果要在二进制文件中读取和写入文本内容，请确保进行编码和解码操作
"""
with open('something.bin', 'rb') as f:
    data = f.read()
# b'Hello,World'  表示的是字节串
with open('something.bin', 'wb') as f:
    f.write(b'Hello,World')

with open('something.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('something.bin', 'wb') as f:
    text = 'Hello,World'
    f.write(text.encode('utf-8'))
