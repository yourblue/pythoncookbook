"""
在集合中找到最大或最小的N个元素
heapq可以处理这个问题

还可以使用heapq.heapify把序列变成一个堆
堆的特性，items[0]总是最小的那个元素
如果只想要找最大值或者最小值，用max或者min比较合适
"""
import heapq

nums = [1, 8, 0, 23, 4, 1, 6, -3, 89, -90, 34, 22]
print(heapq.nlargest(2, nums))
print(heapq.nsmallest(3, nums))

head=list(nums)
heapq.heapify(head)
print(heapq.heappop(head))
print(heapq.heappop(head))
