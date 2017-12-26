import os
import fnmatch
import gzip
import bz2
import re


def gen_find(file_path, top):
    """
    Find all file_names in a directory tree that match a shell wildcard pattern
    :param file_path:
    :param top:
    :return:
    """
    for path, dir_list, file_list in os.walk(top):
        for name in fnmatch.filter(file_list, file_path):
            yield os.path.join(path, name)


def gen_opener(file_names):
    """

    :param file_names:
    :return:
    """
    for filename in file_names:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """

    :param iterators:
    :return:
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """

    :param pattern:
    :param lines:
    :return:
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)
