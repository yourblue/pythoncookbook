CHUNK_SIZE = 8192


def reader(s):
    for chunk in iter(lambda: s.recv(CHUNK_SIZE), b''):
        pass
