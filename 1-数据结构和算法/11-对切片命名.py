"""
清理切片索引
切片会包含start但是不包含stop
"""
items = [0, 1, 2, 3, 4, 5, 6, 7]
a = slice(2, 4)  # 给切片命名
print(items[2:4])
print(items[a])
print(a.start)
print(a.stop)
print(a.step)

s='HelloWorld'

print(a.indices(len(s)))
print(*a.indices(len(s)))
print(range(*a.indices(len(s))))
for i in range(*a.indices(len(s))):
    print(s[i])