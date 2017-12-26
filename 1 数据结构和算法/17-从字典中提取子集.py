"""
从一个字典中提取子集
字典推导式（正常情况下使用这种方案最快，也最直观）
"""
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
p1 = {key: value for key, value in prices.items() if value > 50}
print(p1)
