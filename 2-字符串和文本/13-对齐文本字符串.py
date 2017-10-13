text = 'HelloWorld'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.ljust(20,'-'))
print(text.rjust(20,'+'))
print(text.center(20,'-'))
print(format(text,'=>20'))
print(format(text,'=<20'))
print(format(text,'=^20'))
#format()不特定于str。能作用于任何值
