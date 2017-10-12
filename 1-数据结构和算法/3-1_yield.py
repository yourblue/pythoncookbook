"""
迭代：创建一个列表，然后逐一遍历，这就是迭代。可以使用"for...in..."。处理的都是可迭代对象（迭代是把数据存到内存中）
生成器：生成器是迭代器，可以使用"for...in..."操作。这个操作并没有放到内存中，而是实时生成的。生成器只能操作一次。
yield：是一个关键词，类似return，但是他返回的是一个生成器。
当你调用这个函数的时候，函数内部的代码并不立马执行
"""


def countdown(n):
    print("start to count", n)
    while n > 0:
        yield n
        n -= 1
        # print(n)
    print("done")


if __name__ == '__main__':
    c = countdown(3)
    # print(c)
    for a in c:
        print("a:" + str(a))
    print(c)
    # next(c)
    for b in c:
        print("b:" + str(b))
    else:
        print("没有执行哦")
