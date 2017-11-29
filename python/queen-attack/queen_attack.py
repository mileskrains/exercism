def board(white_position, black_position):
    board = [['_']*8]*8
    for (r, c), ch in zip((white_position, black_position), ('W', 'B')):
        if min(r, c) < 0 or max(r, c) > 7 or white_position==black_position:
            raise ValueError
        rm = board[r][:]
        rm[c] = ch
        board[r] = rm
    return list(map(lambda r: ''.join(r), board))


def can_attack(white_position, black_position):
    wr, wc = white_position
    br, bc = black_position
    if min(wr, wc, br, bc) < 0 or max(wr, wc, br, bc) > 7 or (wr, wc)==(br, bc):
        raise ValueError
    return wr==br or wc==bc or abs(wr-br)==abs(wc-bc)
