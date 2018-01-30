import sys

"""
rt:读取
wt:写入，但是会清除并覆盖原先的内容
at:在已存在的文件结尾添加内容，
"""
with open('../files/file.txt', 'rt', newline="") as f:
    # data = f.read()
    # print(data)
    for line in f:
        print(line)
# 获取默认字符编码
print(sys.getdefaultencoding())
