import math

"""
python中要通过float()来创建无穷大和nan这样的特殊值
"""
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)
# 检测要使用math.isinf()和math.isnan()
print(math.isinf(a))
print(math.isnan(c))
# nan会通过所有的操作进行传播，并且两个nan也不是相等的
# 无穷大也会在计算中进行传播，并且有些操作会产生nan
