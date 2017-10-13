"""
查找和替换文本
"""
# 简单的替换直接使用
text = 'qiuhaiyang,today is 2017/10/12'
text = text.replace('qiu', 'yang')
print(text)
# 复杂一点的要使用re.sub()
import re

# text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\1-\2-\3', text)  # \1这样的形式代表了模式中捕获组的数量
# print(text)
# 先将模式编译可以获得更好的性能
datepet = re.compile(r'(\d+)/(\d+)/(\d+)')
datepet.sub(r'\1-\2-\3', text)
n, m = datepet.subn(r'\1-\2-\3', text)  # 可以统计完成多少次替换
print(n)
print(m)
