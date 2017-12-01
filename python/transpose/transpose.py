from itertools import zip_longest

def transpose(input_lines):
    if input_lines == '':
        return ''
    if type(input_lines) == str:
        input_lines = [input_lines]
    inp = [line.replace(' ', '~') for line in input_lines]
    transpose = list(map(lambda z: ''.join(z),
                         zip_longest(*inp, fillvalue=' ')))
    transpose = [line.rstrip().replace('~', ' ') for line in transpose]
    if len(transpose) == 1:
        transpose = transpose[0]
    return transpose
