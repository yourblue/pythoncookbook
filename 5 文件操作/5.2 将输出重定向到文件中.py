"""
将print()函数的输出重定向到文件中，但是要确保这个文件是以文本模式打开的，如果是以二进制模式打开的，就会报错
"""
with open('../files/file.txt', 'at') as f:
    print('\nHello,World', file=f)
