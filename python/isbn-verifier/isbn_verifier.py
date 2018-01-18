def verify(isbn):
    digs = [int(ch) if ch.isdigit() else 10
            for ch in isbn
            if ch.isdigit() or ch=='X']
    if (len(digs) != 10 or
        10 in digs[:9] or
        not (isbn[-1].isdigit() or isbn[-1]== 'X')):
        return False
    return sum([d * (10 - i) for i, d in enumerate(digs)]) % 11 == 0