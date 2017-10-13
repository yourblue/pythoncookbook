import re

text = 'UPPER PYTHON,lower python,Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
re.sub('python', 'snake', text, flags=re.IGNORECASE)  # 有一个问题，替换后的大小写不匹配


def match_case(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


text = re.sub('python', match_case('snake'), text, flags=re.IGNORECASE)
print(text)
