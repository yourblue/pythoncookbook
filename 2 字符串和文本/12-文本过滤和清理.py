"""
性能：
简单的替换操作：str.replace()最快
高级的操作：str.translate()比较快
"""
s = 'pyth^on\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
print(s.translate(remap))
import sys
import unicodedata

print(sys.maxunicode)
print(sys.maxsize)
cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

