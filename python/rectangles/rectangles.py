from itertools import combinations

def update_tracker(tracker, col, lines):
    start_row, end_row, closed_ct, open_ct, continuing = tracker
    subcol = ''.join(line[col] for line in lines[start_row:end_row+1])
    if (subcol.startswith('+') and
        subcol.endswith('+') and
        ' ' not in subcol and
        '-' not in subcol):
        if continuing:
            closed_ct += open_ct
        open_ct += 1
        continuing = True
    elif continuing and subcol[0] in '+-' and subcol[-1] in '+-':
        continuing = True
    else:
        open_ct = 0
        continuing = False
    return (start_row, end_row, closed_ct, open_ct, continuing)


def count(lines):
    corner_rows = [rn for rn, r in enumerate(lines) if '+' in r]
    if corner_rows == []:
        return 0

    trackers = [(start_row, end_row, 0, 0, False)
                for start_row, end_row in combinations(corner_rows, 2)]

    for col in range(len(lines[0])):
        trackers = [update_tracker(tr, col, lines) for tr in trackers]

    return sum([tr[2] for tr in trackers])

