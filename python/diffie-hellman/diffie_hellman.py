import random


def fermat_primality_test(number):
    for _ in range(3):
        rn = random.randint(2, number)-1
        if pow(rn, number-1, number) != 1:
            return False
    return True


def private_key(p):
    r = random.randint(2, p-1)
    while not fermat_primality_test(r):
        r = random.randint(2, p-1)
    return r


def pow_mod(x, y, z):
    "Calculate x**y % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def public_key(p, g, private):
    return pow_mod(g, private, p)


def secret(p, public, private):
    return pow_mod(public, private, p)

