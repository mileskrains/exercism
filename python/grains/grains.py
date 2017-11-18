def on_square(integer_number):
    if not 1 <= integer_number <= 64:
        raise ValueError
    return 2**(integer_number - 1)

def total_after(integer_number):
    if not 1 <= integer_number <= 64:
        raise ValueError
    return sum([2**n for n in range(integer_number)])
