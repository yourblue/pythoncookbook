"""
通配符模式匹配
"""
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.TXT'))  # 不区分大小写，但是会根据系统来辨别，在unix系统上回区分大小写

print(fnmatchcase('foo.txt', '*.TXT'))  # 如果要明确区分大小写，应该用这个
