def encode(numbers):
    result = []
    for number in numbers:
        result.extend(_encode(number))
    return result

def _encode(number):
    as_bin = bin(number)[2:]
    parts = []
    while as_bin:
        end = as_bin[-7:]
        as_bin = as_bin[:-7]
        cbit = '1' if parts else '0'
        as_hex = cbit + end.rjust(7, '0')
        parts = [as_hex] + parts
    return list(map(lambda b: int(b, 2), parts))


def decode(bytes_):
    numbers = []
    bin_strs = [bin(byt)[2:].rjust(8, '0') for byt in bytes_]
    accum = ''
    for bs in bin_strs:
        if bs[0] == '1':
            accum += bs[1:]
        else:
            accum += bs[1:]
            numbers.append(int(accum, 2))
            accum = ''
    if accum != '':
        raise ValueError('incomplete sequence')
    return numbers

