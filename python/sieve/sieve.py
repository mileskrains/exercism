import math


def sieve(limit):
    if limit < 2:
        return []
    vals = list(range(2, limit+1))
    term = math.sqrt(limit)
    cpos = 0
    cv = vals[cpos]
    while cv < term:
        vals = [val for val in vals if val==cv or val%cv != 0]
        cpos += 1
        cv = vals[cpos]

    return vals
