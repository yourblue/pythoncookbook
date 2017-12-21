"""
从序列中随机选出元素或者生成随机数
random模块
马特赛特旋转算法（也称梅森旋转算法），是一个确定性算法，但是可以通过random.seed()函数来修改初始化种子值
random还可以用来计算均匀分布，高斯分布，和其他概率分布的函数，但是不应该用于加密处理相关的程序中
"""
import random as rd

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(rd.choice(values))
print(rd.choices(values))
print(rd.sample(values, 4))
rd.shuffle(values)
print(values)
print(rd.randint(1, 999))
print(rd.random())
