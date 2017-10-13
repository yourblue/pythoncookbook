import unicodedata

s1 = 'aaaask\u00f1o'
t1 = unicodedata.normalize('NFC', s1)
"""
NFC:如果可以就是用单个代码点
NFD:每个字符都应该分解开
"""
