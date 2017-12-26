from collections import defaultdict

my_list = ['x', 'z', 'c']
for index, value in enumerate(my_list, 1):
    print(index, value)


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}:Parse error:{}'.format(lineno, e))


#
# word_summary = defaultdict(list)
# with open('myfile.txt', 'r') as f:
#     lines = f.readlines()
# for idx, line in enumerate(lines):
#     words = [w.strip().lower() for w in line.split()]
#     for word in words:
#         word_summary[word].append(idx)

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
# 如果直接用for n,x,y in enumerate(data)这样的话会出错
for n, (x, y) in enumerate(data):
    print(n, (x, y))
