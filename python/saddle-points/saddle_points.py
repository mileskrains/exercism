def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError('matrix is not square')
    columns = list(zip(*matrix))
    sad_pts = set()
    for r, row in enumerate(matrix):
        for c, col in enumerate(columns):
            e = row[c]
            if e == max(row) and e == min(col):
                sad_pts.add((r, c))
    return sad_pts
