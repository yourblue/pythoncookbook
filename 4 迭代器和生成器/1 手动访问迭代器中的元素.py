"""
需要手动访问可迭代对象中的元素的时候

手动访问可迭代的对象的时候，最后没有元素的时候会报一个StopIteration异常
"""
with open('/etc/password') as f:
    try:
        while True:
            # line = next(f)
            line = next(f, None)  # 手动返回一个值
            print(line, end='')
    except StopIteration:
        pass

items = [1, 2, 3]
it = iter(items)
print(next(it))
