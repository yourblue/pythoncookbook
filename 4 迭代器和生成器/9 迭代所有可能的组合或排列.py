import itertools
"""
当面对看起来很复杂的迭代问题的时候，应该尽量先考虑itertools模块
"""
items = ['a', 'b', 'c']
# print(itertools.permutations(items))
# for p in itertools.permutations(items):
#     print(p)

# for p in itertools.combinations(items, 2):
#     print(p)

for p in itertools.combinations_with_replacement(items, 3):
    print(p)
