text = 'foo=23+42*10'
"""
分词处理要先定义出所有可能的标记包括空格
"""
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo=42')
scanner.match()
