"""
同时对数据进行转换和换算
使用生成器表达式
"""
values = [1, 8, 0, 23, 4, 1, 6, -3, 89, -90, 34, 22]
s = sum(x for x in values)
print(s)