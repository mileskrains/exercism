import math

def primes_up_to(limit=100):
    mask = [True for _ in range(int(limit)+1)]
    mask[:2] = [False] * 2
    for n in range(2, int(round(math.sqrt(limit), 0)+1)):
        m = 2
        while m * n <= limit:
            mask[m*n] = False
            m += 1
    return [p for p, m in enumerate(mask) if m]
        
def prime_factors(natural_number):
    factors = []
    for step in range(2):
        if step == 0:
            poss_factors = primes_up_to(math.sqrt(natural_number))
        else:
            poss_factors = primes_up_to(natural_number)
        for p in poss_factors:
            while natural_number % p == 0:
                factors.append(p)
                natural_number /= p
            if natural_number == p:
                factors.append(p)
                break 
    return factors
