"""
查找和替换文本
"""
# 简单的替换直接使用
text = 'qiuhaiyang,today is 2017/10/12'
text = text.replace('qiu', 'yang')
print(text)
# 复杂一点的要使用re.sub()
import re

text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\1-\2-\3', text)
print(text)
