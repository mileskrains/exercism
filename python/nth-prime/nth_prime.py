import math


def primes_up_to(limit=100, primes=[2]):
    if limit < primes[-1]:
        return primes
    mask = [True for _ in range(int(1.1*limit)+1)]
    mask[:2] = [False] * 2
    for n in range(2, int(round(math.sqrt(1.1*limit), 0)+1)):
        m = 2
        while m * n <= limit:
            mask[m*n] = False
            m += 1
    new_primes = [p for p, m in enumerate(mask) if m and p > primes[-1]]
    primes.extend(new_primes)
    return primes


def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError('argument must be integer >= 1')
    x = 100
    while x/math.log(x) < positive_number:
        x *= 2
    primes = primes_up_to(x)
    return primes[positive_number-1]
