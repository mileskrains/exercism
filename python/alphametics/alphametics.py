from itertools import permutations


def solve(puzzle):
    lhs, rhs = puzzle.split(' == ')
    lhs = lhs.split(' + ')
    letters = set(list(rhs))
    nonzero = set(rhs[0])
    for term in lhs:
        letters.update(list(term))
        nonzero.add(term[0])
    conv_keys = list(letters-nonzero) + list(nonzero)
    perms = permutations('0123456789', len(letters))
    for perm in perms:
        conv_dict = dict(zip(conv_keys, perm))
        if '0' in perm[-len(nonzero):]:
            continue
        if eval(''.join([conv_dict[c] if c.isalpha() else c for c in puzzle])):
            return {k: int(v) for k, v in conv_dict.items()}
    return {}

