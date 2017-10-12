"""
需要从某个可迭代对象（任意长度）中分解出N个元素
*表达式，可以很方便的解决这个问题
个人理解：Python会识别用户输入的结构，从而确定*表达式要取的值的范围
无论*表达式要取的值是否存在，*变量一直是一个list

Python在内部对递归做了限制，因此Python并不适合处理递归
"""
from audioop import avg


def drop_first_last(grades):
    """
    求课程平均分，去掉最高分，去掉最低分
    :param grades: 课程分数序列
    :return: 平均分
    """
    first, *middle, last = grades
    return avg(*middle)
