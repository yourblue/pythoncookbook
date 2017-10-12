"""
按照特定的文本模式进行匹配和查找
"""

# 简单的文字匹配
text = 'qiuha,iya8n2g'
text.find('hai')
text.endswith('yang')
text.startswith('qiu')
# 稍微复杂一点的可以使用正则表达式
import re

print(re.match(r'\d', text))  # match会匹配字符串的开头，

# 在整个文本搜索就要用findall()了
print(re.findall(r'\d', text))
for i in re.findall(r'\d', text):
    print('1'+i)
print(re.finditer(r'\d', text))
for j in re.finditer(r'\d', text):
    print(j)