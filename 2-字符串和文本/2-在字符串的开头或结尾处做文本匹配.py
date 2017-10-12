"""
在字符串的开头或结尾按照指定的文本模式检查

"""
import os

files_name = os.listdir('.')
print(files_name)
print([name for name in files_name if name.endswith(('.py', '.html'))])  # 如果有多个选项的话，必须要是元组
print(any([name for name in files_name if name.endswith(('.py', '.html'))]))
