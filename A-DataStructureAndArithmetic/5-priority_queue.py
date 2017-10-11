"""
实现一个能够根据给定的优先级来对元素排序，并且每次pop操作都返回优先级最高的那个元素


"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 2)
    q.push(Item('span'), 4)
    q.push(Item('br'), 5)
    q.push(Item('hr'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
