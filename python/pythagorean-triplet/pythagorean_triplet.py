import itertools
import math


def triplets_in_range(range_start, range_end):
    triplets = []
    for c in range(range_start, range_end+1):
        for a in range(range_start, c):
            b = math.sqrt(c**2 - a**2)
            if b >= range_start and b == int(b):
                triplets.append(tuple(sorted([a, int(b), c])))
    return set(sorted(triplets))


def prime_factorization(num):
    factors = []
    for n in range(2, num+1):
        while num % n == 0:
            factors.append(n)
            num /= n
        if num == 1:
            break
    return factors


def triplet_is_coprime(triplet):
    factors_list = [list(set(prime_factorization(n))) for n in triplet]
    flattened = list(itertools.chain(*factors_list))
    return len(flattened) == len(set(flattened))


def primitive_triplets(b):
    if b % 4:
        raise ValueError
    triplets = []
    for c in range(3, int(b**2/4)+2):
        a_squared = c**2 - b**2
        if a_squared > 8:
            a = math.sqrt(a_squared)
            if a == int(a) and triplet_is_coprime((int(a), b, c)):
                triplets.append(tuple(sorted([int(a), b, c])))
    return set(sorted(triplets))


def is_triplet(triplet):
    a, b, c = sorted(list(triplet))
    return a**2 + b**2 == c**2
