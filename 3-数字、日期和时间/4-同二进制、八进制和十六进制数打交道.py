x = 1234
# 将一个整数转化成对应进制的文本字符串形式，使用内建的进制函数
print(bin(x))
print(oct(x))
print(hex(x))
print(format(x, 'b'))  # 不会带有进制的特有前缀
print(format(x, 'o'))
print(format(x, 'x'))
# 要将字符串形式的整数转化为不同的进制，需要使用int()函数加上对应的进制
print(int("111111001", 10))
