import fractions

"""
fractions可以用来对分数进行运算
"""
a = fractions.Fraction(5, 4)
b = fractions.Fraction(7, 16)
print(a + b)

# getting numerator/denominator
c = a * b
print(c.numerator)
print(c.denominator)

# to a float
print(float(c))

# to a fraction
x = 3.75
y = fractions.Fraction(*x.as_integer_ratio())
print(y)
