import os

if not os.path.exists('../files/something'):
    with open('../files/something','wt') as f:
        f.write('Hello\n')
else:
    print('File already exist')
