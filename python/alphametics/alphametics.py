from itertools import permutations


def solve(puzzle):
    words = [w for w in puzzle.split() if w.isalpha()]
    nonzero = set([w[0] for w in words])
    letters = list(set(''.join(words))-nonzero) + list(nonzero)
    perms = permutations('0123456789', len(letters))
    for perm in perms:
        conv_dict = dict(zip(letters, perm))
        if '0' in perm[-len(nonzero):]:
            continue
        if eval(''.join([conv_dict[c] if c.isalpha() else c for c in puzzle])):
            return {k: int(v) for k, v in conv_dict.items()}
    return {}
