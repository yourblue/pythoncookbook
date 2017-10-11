"""
字典的各种计算
zip创建的是一个迭代器
"""
if __name__=="__main__":
    prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
    print(min(zip(prices.values(), prices.keys())))
    print(max(zip(prices.values(), prices.keys())))
    print(sorted(zip(prices.values(), prices.keys())))
