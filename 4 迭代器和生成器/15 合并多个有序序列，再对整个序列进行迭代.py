import heapq
"""
heapq对所有提供的序列都不会做一次性读取
要使用这个函数，必须是有序的
"""
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
