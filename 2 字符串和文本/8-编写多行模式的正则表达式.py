"""
能够跨越多行匹配的正则表达式
"""
import re

comment = re.compile(r'/\*(.*?)\*/')
comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
text1 = '''/*this is a 
comment*/'''
text2 = '/* this is a comment */'
print(comment1.findall(text1))
print(comment.findall(text2))
