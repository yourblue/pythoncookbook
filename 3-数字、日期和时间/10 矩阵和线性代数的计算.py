"""
同样使用NumPy，里面有一个matrix对象可以来处理这种情况
"""
import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 6], [9, -10, 2]])
print(m.A)
print(m.A1)
print(m.H)
print(m.T)
