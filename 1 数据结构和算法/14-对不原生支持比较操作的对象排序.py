"""
对不原生支持比较操作的对象排序

"""
from operator import attrgetter

"""
attrgetter同itemgetter 
"""
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(3), User(23), User(89), User(45)]
print(users)
print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=attrgetter('user_id')))
