"""
保留有限的历史记录
collections.deque可以完美解决这个问题
运行速度比list的处理快得多，时间复杂度O(1)
deque指定的maxlen应该是下标数字，从0开始到maxlen
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('../files/file.txt') as f:
        for line, prev_lines in search(f, 'python', 4):
            for p_line in prev_lines:
                print(p_line, end='')
            print(line, end='')
            print('-' * 20)
