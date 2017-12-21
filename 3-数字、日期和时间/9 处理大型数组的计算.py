"""
对大型数据集比如数组和网格进行计算
对于任何涉及数组的计算密集型任务，请使用NumPy库
import numpy as np 是一种常见的导入方式
"""
import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([9, 25, 36, 16])
print(ax * 8)
print(ax * ay)
print(np.sqrt(ay))
grid = np.zeros(shape=(10, 10), dtype=int)
print(grid + 10)
print(grid[1])
print(grid[:, 1])
