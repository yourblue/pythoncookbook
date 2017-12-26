"""
找出两个字典中可能相同的地方
只要通过keys()和items()执行常见的集合操作就行了。但是values()不可以进行集合操作，因为value的值不是唯一的。
常见的集合操作：
&   交集
|   并集
-   差集
in  属于
==  相等
"""
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
print(a.items() | b.items())
