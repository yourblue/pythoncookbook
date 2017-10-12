"""
需要提取某些值或者对序列做删减
1、列表推导式     ->      原始输入很大的话会生成一个庞大的结果
2、生成器表达式    ->     通过迭代的方式产生筛选结果
列表推导式和生成器表达式的区别就是中括号和小括号
对于复杂的筛选，可以自建函数
"""
from itertools import compress
"""
两个参数，一个可迭代对象，一个布尔选择器序列（正常生产过程中，应该是和可迭代对象中的数据对应的，或者属于其中的一部分）
"""
values = [1, 8, 0, 23, 4, 1, 6, -3, 89, -90, 34, 22]
print([n for n in values if n > 0])
print((n for n in values if n > 0))


def is_int(item):
    try:
        x = int(item)
        return True
    except ValueError:
        return False


print(list(filter(is_int, values)))
