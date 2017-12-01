from itertools import zip_longest


def transpose(input_lines):
    if not input_lines:
        return ''
    inp = [line.replace(' ', '~') for line in input_lines.split('\n')]
    transpose = list(map(lambda z: ''.join(z),
                         zip_longest(*inp, fillvalue=' ')))
    transpose = [line.rstrip().replace('~', ' ') for line in transpose]
    return '\n'.join(transpose)
