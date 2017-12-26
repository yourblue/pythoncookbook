"""
反向迭代只有在待处理的对象拥有可确定的大小或者对象实现了__reversed__()特殊方法的时候才有效。

否则就需要先把可迭代对象转化成列表，但是这个操作是非常消耗内存的
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


c = Countdown(3)
for a in c.__reversed__():
    print(a)
