"""
需要将字符串差分成不同的字段，但是分隔符在字符串中不一致
"""
import re

lines = 'asd,qwe;fasd oqidj6alks,qwe,lll'
print(re.split(r'[,;\s\d]\s*', lines))
print(re.split(r'(,|;|\s|\d)\s*', lines))
print(re.split(r'(?:,|;|\s|\d)\s*', lines))

