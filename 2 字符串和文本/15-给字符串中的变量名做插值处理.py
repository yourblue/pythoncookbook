"""
如果值全部都有的话，使用format()可以处理，但是不能处理缺少值的情况
"""
s = '{name} has {n} messages'

print(s.format(name='Guide', n=31))

name='Guide'
n=31
print(s.format_map(vars()))
