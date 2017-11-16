import math

def sum_of_multiples(limit, multiplicands):
    multiples = set()
    for m in multiplicands:
        mult_max = math.ceil(limit / m)
        multiples |= set([m*c for c in range(mult_max)])
    return sum(multiples)
