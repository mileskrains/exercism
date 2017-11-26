from itertools import chain, cycle
from collections import defaultdict


def fence_pattern(message_size, rails):
    rail_cycler = cycle(chain(range(1, rails+1), range(rails-1, 1, -1)))
    codedict = defaultdict(list)
    for k,v in zip(rail_cycler, range(message_size)):
        codedict[k].append(v)
    return list(chain(*codedict.values()))


def encode(message, rails):
    fp = fence_pattern(len(message), rails)
    return ''.join([message[i] for i in fp])


def decode(encoded_message, rails):
    fp = fence_pattern(len(encoded_message), rails)
    message = [None] * len(encoded_message)
    for i,c in zip(fp, encoded_message):
        message[i] = c
    return ''.join(message)