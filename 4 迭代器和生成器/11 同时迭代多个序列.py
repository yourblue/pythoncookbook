xpts = [1, 2, 3, 4, 5]
ypts = [6, 7, 8, 9, 0, 10]
# 输出的序列长度和最短的序列长度一样
for x, y in zip(xpts, ypts):
    print(x, y)

from itertools import zip_longest

# 可以填充某个序列中不够的值为制定的值
for x, y in zip_longest(xpts, ypts, fillvalue=0):
    print(x, y)
# zip创建的是一个迭代器，要保存数据的话，要转变成list