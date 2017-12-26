import itertools

with open('/etc/password') as f:
    for line in itertools.dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

items = ['a', 'b', 'c', 'd', 1, 2, 3, 4]
for x in itertools.islice(items, 3, None):
    print(x)


