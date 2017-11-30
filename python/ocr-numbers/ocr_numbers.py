def convert(input_grid):
    line_lens_vary = len(set(map(len, input_grid))) != 1
    if line_lens_vary or len(input_grid) % 4 != 0 or len(input_grid[0]) % 3 != 0:
        raise ValueError
    segs_to_digit = {(' _ ', '| |', '|_|', '   '): '0',
                     ('   ', '  |', '  |', '   '): '1',
                     (' _ ', ' _|', '|_ ', '   '): '2',
                     (' _ ', ' _|', ' _|', '   '): '3',
                     ('   ', '|_|', '  |', '   '): '4',
                     (' _ ', '|_ ', ' _|', '   '): '5',
                     (' _ ', '|_ ', '|_|', '   '): '6',
                     (' _ ', '  |', '  |', '   '): '7',
                     (' _ ', '|_|', '|_|', '   '): '8',
                     (' _ ', '|_|', ' _|', '   '): '9'}
    row_ct = len(input_grid)//4
    out = []
    for drn in range(row_ct):
        dig_row = input_grid[drn*4:drn*4+4]
        row_digits_ct = len(dig_row[0])//3
        row = ''
        for rdn in range(row_digits_ct):
            digit = [line[rdn*3:rdn*3+3] for line in dig_row]
            row += segs_to_digit.get(tuple(digit), '?')
        out.append(row)
    return ','.join(out)
