def star_ct(r, c, inp):
    row_ct = len(inp)
    col_ct = len(inp[0])
    stars = 0
    for ri in [r-1, r, r+1]:
        for ci in [c-1, c, c+1]:
            if 0 <= ri < row_ct and 0 <= ci < col_ct:
                if inp[ri][ci] == '*':
                    stars += 1
    return str(stars) if stars else ' '

def board(input_board_array):
    if len(set(map(len, input_board_array))) > 1:
        raise ValueError('rows are not of equal length')
    out = []
    for r, row in enumerate(input_board_array):
        out_row = []
        for c, val in enumerate(row):
            if val == ' ':
                out_row.append(star_ct(r, c, input_board_array))
            elif val == '*':
                out_row.append('*')
            else:
                raise ValueError('invalid char encountered')
        out.append(''.join(out_row))
    return out