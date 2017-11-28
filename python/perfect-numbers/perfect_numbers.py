from functools import reduce
from itertools import combinations
from operator import mul
    

def prime_factors(n):
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    p = 3
    while n > 1:
        while n % p == 0:
            result.append(p)
            n //= p
        p += 2
    return result


def classify(number):
    if number < 1:
        raise ValueError
    if number > 1:
        prime_facs = prime_factors(number)
        facs = set()
        for n in range(1, len(prime_facs)):
            facs.update(set(combinations(prime_facs, n)))
        aliquot_sum = sum([reduce(mul, fl) for fl in facs]) + 1
        if aliquot_sum > number:
            return 'abundant'
        elif aliquot_sum == number:
            return 'perfect'
    return 'deficient'


# grabbed code from @3xpl0r3r for speed comparison ... (it is ~31x faster!) 
def classify(number):
    factors = list()
    total = 0

    if number <=0:
        raise ValueError

    for i in range(1, int(number ** 0.5+1)):
        if number % i == 0:
            if (i != number / i):               
                factors.append(i)
                factors.append(number / i)
            else:
                factors.append(i)
    factors.remove(number)
    total = sum(factors)

    if total == number:
        return("perfect")
    elif total > number:
        return("abundant")
    else:
        return("deficient")
