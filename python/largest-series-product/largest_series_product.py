from operator import mul
from functools import reduce


def largest_product(series, size):
    if size == 0:
        return 1
    if size < 0 or size > len(series) or not series.isdigit():
        raise ValueError
    tp = 0
    for i in range(len(series)-size+1):
        tp = max(tp, reduce(mul, [int(c) for c in series[i:i+size]]))
    return tp
