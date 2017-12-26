"""
正则表达式对文本的匹配，但是匹配出来的是最长的可能匹配，想找出最短的可能匹配
*操作符在正则表达式中采用的是贪心策略
在*或者+后面添加一个？会强制将匹配算法调整为最短的可能匹配
"""
import re

str_pat = re.compile(r'\"(.*?)\"')
text1 = 'Computer say "no.",Phone say "yes."'
print(str_pat.findall(text1))
