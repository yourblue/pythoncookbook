"""
创建类似文件的对象,使用io.StringIO()和io.BytesIO(),后者专门操作二进制文件
StringIO和BytesIO实例是没有真正的文件描述符来对应的，因此他们没法工作在一个需要真正的系统级文件的代码环境中的
"""
import io

s = io.StringIO()
s.write('Hello,World\n')
print('this is a test', file=s)
# print(s.getvalue())
# print(s.read(4))
# print(s.read())
b = io.BytesIO()
b.write(b'binary data')
print(b.getvalue())
