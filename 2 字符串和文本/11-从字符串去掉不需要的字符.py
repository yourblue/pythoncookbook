s = '--hello   world++ \n'
print(s.strip())
print(s.lstrip('-'))
print(s.rstrip('+'))
# 上面的方法只能从开始的地方开始匹配，也不会对位于字符串中间的文本起作用
# 可以使用replace()或者正则表达式代替
import re

print(re.sub('(?:-|\+|\s|\n)+', ' ', s))
