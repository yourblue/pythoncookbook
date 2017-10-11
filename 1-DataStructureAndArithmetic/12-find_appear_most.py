"""
想知道序列中出现次数最多的元素是什么
"""
from collections import Counter
"""
Counter可以接收任何可哈希的序列作为输入，可以使用数学计算
适应范围：需要对数据制表或计数的问题
"""
words = 'yangfangyu,qiuhaiyangxihuanni,nizhidaoma'
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
