def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(1, 4, 0.5):
    print(n)

print(list(frange(1, 4, 1)))


def countdown(no):
    print('Starting to count from', no)
    while no > 0:
        yield no
        no -= 1
    print('Done')
